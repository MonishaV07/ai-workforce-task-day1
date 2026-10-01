# Day 2 – Reasoning and Acting

## 1. Scenario

The scenario selected for this experiment is a College Technical Event
Budget Assistant.

A college technical event has a total budget of ₹5,000.

The expenses are:

- Venue: ₹1,500
- Certificates: ₹800
- Refreshments: ₹1,200

There are 30 students attending.

The scenario contains both reasoning-only questions and a question
requiring external information.

The reasoning questions involve calculating the remaining budget and
dividing the remaining amount among the students.

The external-information question asks for the current USD to INR
exchange rate. This information is obtained through an external
exchange-rate tool.

A combined question asks for the INR value of a $20 prize using the
current exchange rate.

---

## 2. Direct Prompting

Direct prompting sends the user's question directly to the language
model and produces an answer without using an external tool.

In this experiment, the direct prompting approach was used for the
event budget calculation.

The model receives the budget information and directly produces the
answer.

The flow is:

Question → Language Model → Final Answer

The main advantage of direct prompting is speed and simplicity.
However, it does not provide external information through a tool in
this experiment.

For example, if the question requires the current USD to INR exchange
rate, direct prompting cannot reliably retrieve the current value
without external tool access.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting is used for questions involving multiple
reasoning steps.

In this scenario, the model must first determine the remaining event
budget and then divide that amount among 30 students.

The reasoning process can be represented as:

Question → Multi-step reasoning → Final Answer

The approach can be useful for calculations and logical problems
because the model is encouraged to work through the problem carefully.

However, reasoning alone does not give the model access to current
external information.

Therefore, Chain-of-Thought can reason about a supplied exchange rate,
but it cannot independently obtain the current exchange rate unless a
tool is provided.

---

## 4. ReAct Agent

The ReAct approach combines reasoning with actions.

In this experiment, the ReAct agent receives a question asking for
the current INR value of a $20 prize.

The agent recognizes that it needs current exchange-rate information.

It therefore calls the external exchange-rate tool.

The process is:

Thought → Action → Observation → Thought → Final Answer

The tool returns the current USD to INR exchange rate. The agent then
uses that observation to calculate the approximate INR value of the
$20 prize.

This demonstrates an important difference between Chain-of-Thought and
ReAct. Chain-of-Thought can reason over information already available
to the model, while ReAct can interact with an external tool to obtain
additional information.

---

## 5. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Suitable for simple questions | Better suited to multi-step reasoning | Combines reasoning with tool interaction |
| Tool usage | No tool used | No tool used in this experiment | Calls external tools when required |
| Reliability on multi-step questions | Can be sufficient for simple calculations | Can improve multi-step problem solving | Can combine reasoning with external observations |
| Transparency | Final answer is shown | Reasoning explanation can be requested | Tool actions and observations can be traced |
| Speed / cost | Fastest and generally lowest cost | More processing/output | Usually slower because of tool calls |
| Consistency | Depends on temperature and model | Can vary at non-zero temperature | Can vary because reasoning/tool interactions may vary |

---

## 6. Self-Consistency Observation

The Chain-of-Thought reasoning question was executed multiple times
with a non-zero temperature.

The results from the five runs were recorded from the actual program
output.

| Run | Result |
|---|---|
| 1 | TO BE FILLED |
| 2 | TO BE FILLED |
| 3 | TO BE FILLED |
| 4 | TO BE FILLED |
| 5 | TO BE FILLED |

The majority answer was:

**TO BE FILLED**

The majority answer was:

**TO BE FILLED**

When the temperature was changed to 0, the responses became more
deterministic compared with the non-zero-temperature experiment.

The experiment demonstrates that non-zero temperature can introduce
variation between repeated model generations, while temperature 0
generally reduces such variation.

---

## 7. Suitability Analysis

The selected scenario contains both reasoning-only questions and a
question requiring current external information.

Direct prompting is suitable for simple questions where the required
information is already supplied and little reasoning is necessary.

Chain-of-Thought is more appropriate for the multi-step budget
calculation because the model must perform more than one reasoning
operation.

ReAct is particularly suitable for the combined exchange-rate
question because the agent needs information that is not reliably
available from the model's stored knowledge. The agent can call the
external exchange-rate tool, observe its result, and use that
observation to produce the final calculation.

The self-consistency experiment also shows that repeated reasoning
with a non-zero temperature can produce variation. This is useful to
consider when evaluating the consistency of model-generated answers.

---

## 8. Conclusion

Direct prompting is appropriate for simple questions where the model
already has the required information and a direct answer is sufficient.

Chain-of-Thought is useful for problems that require multiple reasoning
steps, such as calculations and logical problems. It can improve the
structure of reasoning but does not independently provide missing
external information.

ReAct is appropriate when a problem requires both reasoning and
interaction with external tools. The agent can determine what
information it needs, call an appropriate tool, observe the result, and
continue reasoning before producing the final answer.

Therefore, the appropriate approach depends on the type of problem.
Direct prompting is useful for simple tasks, Chain-of-Thought for
reasoning-heavy tasks, and ReAct for tasks that combine reasoning with
external information or tool interaction.