import { TavilySearch } from '@langchain/tavily';
import { createAgent } from 'langchain';

const agent = createAgent({
  model: 'gpt-4o',
});

const tool = new TavilySearch({
  maxResults: 5,
  topic: 'general',
});

const result = await agent.invoke({
  messages: [
    { role: 'user', content: 'what is capital of VietNam', tools: [tool] },
  ],
});
console.log('Result:', result.messages[result.messages.length - 1]?.content);
