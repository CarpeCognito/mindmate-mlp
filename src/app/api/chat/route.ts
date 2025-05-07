import { NextResponse } from 'next/server';

const SYSTEM_PROMPT = `
As Mindmate, your responses must follow this structure:

1. **Emotional Resonance**: Validate emotions ("I hear the [emotion]...")
2. **Practical Pathfinding**: 1-3 actionable steps
3. **Psychological Mirror**: Highlight cognitive patterns
4. **Growth Compass**: Link to Mindmate's values
5. **Next-Step Navigation**: Clear now, next, later; close with "Progress over perfection"
`;

export async function POST(req: Request) {
  try {
    const { userMessage } = await req.json();

    // Construct the payload for the Ollama API
    const ollamaPayload = {
      model: 'mistral', // Or 'llama3', whichever you ran
      messages: [
        { role: 'system', content: SYSTEM_PROMPT },
        { role: 'user', content: userMessage },
      ],
    };

    // Call the Ollama API
    const response = await fetch('http://localhost:11434/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(ollamaPayload),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Ollama API Error:', errorData);
      return new NextResponse('Error communicating with local AI', { status: response.status });
    }

    const reader = response.body?.getReader();
    const decoder = new TextDecoder('utf-8');
    let aiMessage = '';
    let streamError = false;

    while (true) {
      const { done, value } = await reader!.read();
      if (done) {
        break;
      }
      const chunk = decoder.decode(value);
      try {
        const jsonChunk = JSON.parse(chunk);
        if (jsonChunk.message?.content) {
          aiMessage += jsonChunk.message.content;
        }
        if (jsonChunk.done) {
          break;
        }
      } catch (e) {
        console.error('Error parsing Ollama chunk:', e, chunk);
        streamError = true; // Set the error flag
        continue; // Skip this chunk
      }
    }

    if (streamError && aiMessage === '') {
      return new NextResponse('Error processing Ollama stream', { status: 500 });
    }

    return NextResponse.json({ message: aiMessage });

  } catch (error) {
    console.error(error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}