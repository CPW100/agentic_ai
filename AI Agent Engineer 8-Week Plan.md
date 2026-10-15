# AI Agent Engineer: 8-Week Plan

Oct 11, 2026 · @Dahlia

This plan takes 2-3 hours a day over 8 weeks (Oct 12 to Dec 6, 2026), ends with a deployed multimodal agent, and has you applying from week 6.

## Plan at a glance

Weekdays run about 2 hours (30 min learn, 75 min build, 15 min notes), weekends 3-4 hours, with one full rest day a week.

| Weeks | Dates (2026) | Focus | Output | Quiz |
| --- | --- | --- | --- | --- |
| 1-2 | Oct 12 - Oct 25 | LLM app basics, tool calling, structured output | Hand-built agent with 3 tools | Checkpoint 1 |
| 3-4 | Oct 26 - Nov 8 | RAG and multimodal (documents and images) | Document Q&A app with citations; vision extraction demo | Checkpoint 2 |
| 5-6 | Nov 9 - Nov 22 | Agent loops, MCP, evals, guardrails | MCP server; eval suite; start applying Nov 16 | Checkpoint 3 |
| 7-8 | Nov 23 - Dec 6 | Capstone deploy, demo video, interview prep | Public demo, README with eval results | Checkpoint 4 and a mock interview |

## Weeks 1-2: LLM basics and tool calling

By Oct 25 you have a hand-built agent with three tools, step limits and run logs, and have passed Checkpoint 1.

### Week 1 (Oct 12 - Oct 18)

- [ ] Mon: Set up Python or TypeScript, get an API key, make a first model call, read how tool calling works.
- [ ] Tue: Get structured output with a JSON schema and validate it (Pydantic or Zod).
- [ ] Wed: Implement one tool and write the tool-call loop by hand, no framework.
- [ ] Thu: Add two more tools, handle malformed arguments by returning errors to the model, add a step limit.
- [ ] Fri: Add streaming and log tokens and cost per run.
- [ ] Sat (3-4h): Refactor into a small CLI agent, push to GitHub with a README.
- [ ] Sun: Rest. Take Checkpoint 1 in chat if you feel like it.

### Week 2 (Oct 19 - Oct 25)

- [ ] Mon: Write system prompts and tool descriptions; test how wording changes tool choice.
- [ ] Tue: Add conversation memory with truncation and summarization.
- [ ] Wed: Add timeouts, retries and idempotency to tools.
- [ ] Thu: Write each step to a JSONL trace and replay a run from it.
- [ ] Fri: Run 10 hand-written test tasks on two models; record where each fails.
- [ ] Sat (3-4h): Polish, record a 1-minute demo, update the README with your findings.
- [ ] Sun: Rest.

## Weeks 3-4: RAG and multimodal

By Nov 8 you have a document Q&A app with citations and a vision extraction demo, which is where your computer vision background shows, and have passed Checkpoint 2.

### Week 3 (Oct 26 - Nov 1)

- [ ] Mon: Learn embeddings and similarity search; embed 50 documents and query them.
- [ ] Tue: Experiment with chunking sizes and overlap; compare retrieval results by hand.
- [ ] Wed: Set up a vector store (pgvector is a good default) and index a real document set.
- [ ] Thu: Add hybrid search (keyword plus vector) and a reranker.
- [ ] Fri: Generate answers with source citations; refuse when retrieval finds nothing.
- [ ] Sat (3-4h): Build a small retrieval test set of 20 questions and measure hit rate.
- [ ] Sun: Rest.

### Week 4 (Nov 2 - Nov 8)

- [ ] Mon: Send images and PDFs to a vision-language model; extract fields to a JSON schema.
- [ ] Tue: Handle messy inputs (rotated scans, low resolution, tables) and log failures.
- [ ] Wed: Add confidence checks: validate totals, dates and required fields against rules.
- [ ] Thu: Route low-confidence extractions to a human review queue.
- [ ] Fri: Combine retrieval and extraction into one agent tool set.
- [ ] Sat (3-4h): Record a demo, write up accuracy on 30 sample documents, take Checkpoint 2.
- [ ] Sun: Rest.

## Weeks 5-6: agents, MCP, evals and guardrails

By Nov 22 you have an MCP server, an eval suite with metrics, basic guardrails, and your first applications out from Nov 16.

### Week 5 (Nov 9 - Nov 15)

- [ ] Mon: Study agent patterns (routing, planning, orchestrator-worker) and when a plain workflow beats an agent.
- [ ] Tue: Rebuild your capstone core as a loop with planning and a step budget.
- [ ] Wed: Learn the Model Context Protocol and build an MCP server exposing two of your tools.
- [ ] Thu: Connect a client to your MCP server and test end to end.
- [ ] Fri: Try one agent framework (LangGraph or an official agent SDK) and note trade-offs against your hand-built loop.
- [ ] Sat (3-4h): Write the first 20 eval cases: expected outcome, allowed tools, max steps, cost limit.
- [ ] Sun: Rest.

### Week 6 (Nov 16 - Nov 22)

- [ ] Mon: Automate evals: run all cases, grade outcomes and tool trajectories, print a summary table.
- [ ] Tue: Add tracing and observability (a hosted tracing tool or your own JSONL plus a viewer).
- [ ] Wed: Add guardrails: treat tool output as untrusted data, least-privilege tool permissions, confirmation for risky actions.
- [ ] Thu: Test prompt injection with a poisoned document and record the result.
- [ ] Fri: Update CV and LinkedIn; apply to 5 roles, including 2 stretch roles.
- [ ] Sat (3-4h): Fix the top 3 eval failures, rerun, record before and after scores. Take Checkpoint 3.
- [ ] Sun: Rest.

## Weeks 7-8: capstone and interview prep

By Dec 6 the capstone is deployed with a public demo, a 2-minute video and a README that shows eval results; you are practicing interviews while applications run.

### Week 7 (Nov 23 - Nov 29)

- [ ] Mon: Containerize the app and deploy it (AWS or similar) with secrets handled safely.
- [ ] Tue: Add authentication, rate limits and a cost cap per run.
- [ ] Wed: Build a simple review UI where a human approves or edits low-confidence results.
- [ ] Thu: Run the full eval suite on the deployed version; fix the worst failures.
- [ ] Fri: Record a 2-minute demo video; write the architecture section of the README.
- [ ] Sat (3-4h): Write a short post covering what failed and what you changed. Take Checkpoint 4.
- [ ] Sun: Rest.

### Week 8 (Nov 30 - Dec 6)

- [ ] Mon: Practice agent system design: draw the architecture, state failure modes and cost trade-offs out loud.
- [ ] Tue: Prepare 3 stories (a bug you debugged, a trade-off you made, a failure you caught with evals).
- [ ] Wed: Do a live coding drill: write a tool-calling loop from scratch in 30 minutes.
- [ ] Thu: Ask me for a mock interview and review the answers.
- [ ] Fri: Tailor your CV for each target track (agent engineer, FDE, AI PM) and follow up on applications.
- [ ] Sat (3-4h): Apply to another 10 roles and book 2 networking chats.
- [ ] Sun: Rest.

## Capstone spec: multimodal document-processing agent

Build an agent that reads invoices or similar business documents (PDFs and photos), extracts structured data, checks it against rules, and sends uncertain cases to a human before anything is saved. I picked finance documents because the work is easy to demo, easy to evaluate and common in Singapore employers' use cases; swap the domain if you prefer.

### Flow

1. A user uploads a PDF or image.
2. The agent classifies the document type and picks an extraction schema.
3. A vision-language model extracts fields into that schema.
4. Validation tools check totals, dates, required fields and a vendor lookup (retrieval over past documents).
5. Low-confidence or rule-failing documents go to a human review queue; the rest are saved.
6. Every step is traced, with token and cost counts.

### Requirements

| Area | Requirement | Done when |
| --- | --- | --- |
| Agent loop | Hand-written loop with a step budget and cost cap | A runaway task stops by itself |
| Tools | At least 4 tools, 2 exposed through your own MCP server | A separate MCP client can call them |
| Retrieval | Vendor and past-document lookup with citations | Answers show which document they came from |
| Human in the loop | Review UI for low-confidence results | A reviewer can approve or edit before saving |
| Evals | 50 labelled documents, outcome and trajectory checks | A single command prints a score table |
| Safety | Poisoned-document test, least-privilege tools | Injection test result is in the README |
| Deployment | Docker, public demo, auth, rate limit | A stranger can try it from a link |

### Eval targets to report in the README

- Field-level accuracy on your labelled set (a starting target is 95% on clean documents; report the real figure).
- Cost per document and 95th percentile latency.
- Share of documents sent to human review.
- Result of the prompt-injection test.

### Suggested stack

Python or TypeScript, FastAPI or similar, Postgres with pgvector, a vision-language model, an MCP server, Docker, and AWS (it matches what many Singapore teams use).

## Resources

These are well-known sources I recommend from memory, not checked live today, so confirm each is still available before you rely on it.

| Phase | Resource | Use it for |
| --- | --- | --- |
| Weeks 1-2 | Tool-use and structured-output docs from your model provider (Anthropic, OpenAI) | Tool calling, JSON schemas, streaming |
| Weeks 1-2 | Anthropic's "Building effective agents" article | When to use workflows versus agents |
| Weeks 3-4 | pgvector documentation | Vector search in Postgres |
| Weeks 3-4 | Hugging Face Agents Course | Agent concepts with built-in quizzes and a certificate |
| Weeks 5-6 | modelcontextprotocol.io documentation | Building MCP servers and clients |
| Weeks 5-6 | LangGraph documentation | One framework to compare against your hand-built loop |
| Weeks 5-6 | Hamel Husain's writing on LLM evals | Practical eval design |
| Weeks 5-6 | OWASP Top 10 for LLM Applications | Prompt injection and other agent security risks |
| Weeks 7-8 | Chip Huyen's book "AI Engineering" | System design vocabulary for interviews |
| Any time | DeepLearning.AI short courses on agents and RAG | Quick structured lessons |

## Interview prep

Practice answering these out loud, using your capstone for every example.

### Agent engineer

- Walk me through your agent loop. How does it stop, and what happens when a tool fails?
- How do you evaluate an agent that gives different outputs on each run?
- Design an agent that processes 10,000 documents a day. Where does cost, latency or failure show up first?
- When would you not use an agent?
- How would you defend against prompt injection from a document the agent reads?
- How do you choose chunk size and retrieval settings, and how do you know they work?

### Forward deployed engineer

- A customer's data is messy and their requirements keep changing. How do you scope a first deployment in two weeks?
- Explain to a non-technical manager why the agent is wrong 5% of the time and what you are doing about it.
- Tell me about a time you debugged a production issue with incomplete information.
- How do you decide between building a custom integration and using what the customer already has?

### AI product manager

- How would you decide whether an AI feature is worth building versus a rules-based approach?
- Which metrics would you track for an agent product beyond accuracy?
- How do you handle a launch when quality is good but not perfect?
- Describe how you would write an eval spec with engineers.

### Your three stories to prepare

1. A bug you debugged in the capstone and how evals caught it.
2. A design trade-off you made (cost versus accuracy, workflow versus agent).
3. A failure you found in testing and the fix, with before and after scores.

## Application tracker

Three leads I found on Oct 11, 2026 to start the table; confirm each is still open before applying, and add your own rows below.

| Company | Role | Track | Notes | Status | Next step |
| --- | --- | --- | --- | --- | --- |
| [3E Accounting](https://www.3ecpa.com.sg/careers/ai-agent-engineer/) | AI Agent Engineer | Agent engineer | Onsite in Novena; posted Aug 31, 2026 | Not applied | Check it is still open |
| [Hiverlab](https://app.semesteria.com/jobs/forward-deployed-engineer-singapore-hiverlab-6737a7c7-5619-4869-abf1-500a9cd8a8aa) | Forward Deployed Engineer | FDE | Onsite, listed near SGD 7K | Not applied | Check it is still open |
| [OpenAI](https://jobs.ashbyhq.com/openai/4c078f82-93b9-427c-8fd8-95de198884b4/application) | Forward Deployed Engineer, Singapore | FDE (stretch) | Not remote; asks for 5+ years of customer-facing work | Not applied | Apply after the capstone is live |

## Job titles and search keywords

Apply mostly to the first row; use the others as secondary tracks.

| Track | Titles to search | Fit with your background |
| --- | --- | --- |
| Agent engineering (main) | AI Agent Engineer, Agentic AI Engineer, Applied AI Engineer, GenAI Engineer, LLM Engineer, AI Engineer, AI Product Engineer, AI Platform Engineer | Strong: 4 years full stack plus deep learning |
| Forward deployed | Forward Deployed Engineer, Solutions Engineer, AI Solutions Engineer, AI Success Engineer, Customer Engineer, Implementation Engineer | Good at mid-level firms; large labs often ask for 5+ years |
| Product | AI Product Manager, Technical Product Manager (AI), Product Manager GenAI, AI Product Owner | Weaker: usually needs product ownership experience |
| Vision-leaning | Computer Vision Engineer, Multimodal Engineer, Applied Scientist | Useful if you want to lean on your deep learning work |

### Where to search

- Singapore: LinkedIn, Jobstreet, MyCareersFuture and company career pages (banks, government tech agencies, global tech offices, startups).
- Global remote: company career pages of AI startups and remote job boards, filtered for roles open in Asia or worldwide.
- Keywords to combine with the titles: agents, LLM, RAG, MCP, tool calling, evals, multimodal, document AI.
