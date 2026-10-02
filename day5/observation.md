# Day 5 Observation Sheet

## 1. Models Used

| Model | Source |
|---|---|
| openai/gpt-oss-20b | Groq API |
| openai/gpt-oss-120b | Groq API |

## 2. Custom Model Experiments

### Fee Assistant
Implemented using a system prompt.

Behavior:
- Does not guess fees.
- Requests lookup when fee information is unavailable.
- Gives short responses.

### Events Announcer
Implemented using a system prompt.

Behavior:
- Produces short college event announcements.
- Uses event name, date, time and venue when provided.

## 3. Prompt Override

A program-level system prompt was used to change the model's behavior,
demonstrating prompt-level customization.

## 4. API Demonstration

The following were tested:

- Model listing
- Chat completion
- Token usage
- Streaming
- Time to first token (TTFT)
- OpenAI-compatible API

## 5. Benchmark

Models compared:

- openai/gpt-oss-20b
- openai/gpt-oss-120b

Benchmark prompts:

1. Reply with exactly: OK
2. In two sentences, what is an AI agent?
3. Scholarship calculation problem

## 6. vLLM Concepts

Studied:

- KV cache
- Static batching
- Continuous batching
- Prefix caching
- Throughput
- Latency

## 7. Implementation Note

The original laboratory uses Ollama for local model serving. This
implementation uses the Groq OpenAI-compatible API instead and therefore
does not claim that Ollama models or Ollama custom models were locally
created.