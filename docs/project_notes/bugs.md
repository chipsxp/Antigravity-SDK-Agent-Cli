# Bug Log

### 2026-06-25 - Context7 Library Identification (Graphiti)
- **Issue**: Attempting to resolve `zep-python` library ID in Context7 returned missing/invalid.
- **Root Cause**: The official library for Zep Graphiti is actually `graphiti-core`, not `zep-python`, which was determined by searching for "Graphiti" instead of the company name.
- **Solution**: Use `graphiti-core` SDK directly for all interactions.
- **Prevention**: Always resolve exact project names rather than broad company/vendor names when querying Context7.

### 2026-06-27 - ADK Agent Synchronous Execution (`App object has no attribute run`)
- **Issue**: Calling `.run()` on the `App` object directly causes an error since `App` does not implement standard synchronous execution. Subsequent attempts to use `InMemoryRunner.run_async()` threw `unexpected keyword argument 'prompt'` or `Session not found`.
- **Root Cause**: ADK Agents must be executed inside a `Runner` context. `run_async` requires a formal `Session` initialization and a fully constructed `types.Content` object for the `new_message` argument. 
- **Solution**: Use `InMemoryRunner(app=...).run_debug(query)` which automatically handles session creation and content wrapping under the hood.
- **Prevention**: Never assume standard LangChain `.run()` patterns for Google ADK. Always reference the runner API.

### 2026-06-27 - MCP stdio Stream Corruption
- **Issue**: MCP client hanging or failing to parse responses from the AI Researcher server.
- **Root Cause**: Interactive Python functions like `input()` and standard `print()` statements output directly to `sys.stdout`. Since the MCP protocol uses standard I/O to communicate JSON-RPC, these statements corrupt the stream.
- **Solution**: Replaced `input()` with environment variable fallbacks (`os.environ.get`) and redirected all prints to `sys.stderr` (`print(..., file=sys.stderr)`).
- **Prevention**: When building MCP servers, standard output is strictly reserved for JSON-RPC messages. Do not use interactive console blocking tools.
