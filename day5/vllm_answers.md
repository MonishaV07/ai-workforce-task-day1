# vLLM Demonstration – Paper-Based Alternative

## 1. Why is KV cache important for LLM serving?

KV cache stores the key and value information from previous tokens during
attention computation. This avoids repeatedly recomputing information for
previous tokens during autoregressive generation and improves serving
efficiency.

## 2. Static batching vs continuous batching

Static batching groups a fixed set of requests together for processing.

Continuous batching dynamically manages requests as they enter and finish,
allowing the server to keep the model hardware more continuously utilized.

## 3. How does prefix caching help repeated prompts?

Prefix caching allows computation associated with a shared prompt prefix to
be reused for later requests with the same prefix. This can reduce repeated
computation and improve efficiency.

## 4. Throughput vs latency

Latency measures the time taken to respond to an individual request.
Throughput measures how much work the serving system can process over a
period of time.

A serving system may need to balance low individual-request latency with
high overall throughput.