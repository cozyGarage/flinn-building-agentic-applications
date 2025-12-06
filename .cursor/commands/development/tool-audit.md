Audit the ReAct agent tools provided alongside this command.

For each tool, analyze:
1. **Context Efficiency**: Does the tool return too much information (e.g., full lists instead of search/pagination)?
2. **Consolidation**: Could this tool be combined with others to reduce round-trips (e.g., search + retrieval)?
3. **Namespacing**: Is the naming convention consistent and distinct (e.g., using prefixes)?
4. **Return Data**: Does it return high-signal, meaningful context versus raw IDs or noisy logs?
5. **Docstrings**: Are the descriptions prompt-engineered to be unambiguous for an LLM?

# Effective Tool Principles for Audit

1. **Context & Efficiency**: 
   - Avoid "list_all" tools that waste context. Prefer `search_*` or `get_*_context` that returns filtered results.
   - Return only high-signal info. Use pagination/truncation for large datasets.
   - Consider a `response_format` parameter (concise vs detailed) to control verbosity.

2. **Consolidation**:
   - Consolidate granular steps. Instead of `get_id` -> `get_details`, use a tool that handles the lookup or returns enriched context immediately.
   - Example: `schedule_event` instead of `find_slot` + `create_event`.

3. **Namespacing**:
   - Use clear prefixes to group related tools (e.g., `recipe_search`, `recipe_view`).
   - Avoid generic names that might overlap with other libraries.

4. **Meaningful Returns**:
   - Resolve opaque IDs (UUIDs) to names/human-readable terms where possible in output.
   - Error messages should be actionable instructions for the model, not just stack traces.

5. **Prompt Engineering**:
   - Tool docstrings are the prompt. Be explicit about inputs (e.g., `user_id` vs `user`).
   - Describe *when* to use the tool, not just *what* it does.

# Output Format

Please output a report in markdown:
- **Tool Name**: [Name]
- **Critique**: [Specific violation or weakness based on principles]
- **Recommendation**: [Concrete code change or refactor idea, e.g., "Rename to X", "Add filtering param", "Merge with Y"]

Finally, provide a **summary of suggested refactors** prioritized by impact.