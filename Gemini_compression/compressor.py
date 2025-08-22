from config import model
import re

# 1. Lexical Compression
def lexical_compression(document: str) -> str:
    """Remove stopwords, redundant words, and compress text lexically."""
    stopwords = {"the", "is", "in", "on", "at", "and", "a", "of", "to"}
    words = document.split()
    compressed = [w for w in words if w.lower() not in stopwords]
    return " ".join(compressed)

# 2. Semantic Compression
def semantic_compression(document: str) -> str:
    """Use Gemini to compress while preserving semantic meaning."""
    response = model.generate_content(
        f"Compress this text by rewriting it in fewer words but preserve the same meaning:\n\n{document}"
    )
    return response.text

# 3. Task-Oriented Compression
def task_oriented_compression(document: str, task: str = "news briefing") -> str:
    """Compress based on a given task (e.g., news briefing, academic abstract)."""
    response = model.generate_content(
        f"Compress this text specifically for the task: {task}. Keep only relevant details:\n\n{document}"
    )
    return response.text

# 4) Map-Reduce Compression — single call, distinct format
def map_reduce_compression(document: str) -> str:
    prompt = f"""
You will perform MAP-REDUCE COMPRESSION.

Step 1 (MAP): Internally split the document into 4–6 logical sections and write ONE 15–25-word micro-summary for each.
Step 2 (REDUCE): Merge those micro-summaries into a single coherent compressed paragraph of 6–9 sentences.

FORMAT STRICTLY:
PARTIALS:
- <micro-summary 1>
- <micro-summary 2>
- <micro-summary 3>
- <micro-summary 4>
- <micro-summary 5>

FINAL:
<single paragraph, no bullets>

DOCUMENT:
{document}
"""
    resp = model.generate_content(prompt)
    return (resp.text or "").strip()


# 5) Latent Compression — returns compact JSON of latent concepts (very different shape)
def latent_compression(document: str) -> str:
    prompt = f"""
Produce a LATENT CONCEPT PACK as compact JSON capturing deep semantics (not surface wording).

Output a single JSON object with these keys ONLY:
  "entities": [top people/orgs/places],
  "themes": [core themes (3–6 words each)],
  "facts": [irreducible facts, short strings],
  "metrics": [numbers/percentages/dates],
  "risks": [top 3 risks, ≤8 words each],
  "actions": [recommended actions, verb-led].

No prose outside JSON. No markdown.

DOCUMENT:
{document}
"""
    resp = model.generate_content(prompt)
    return (resp.text or "").strip()


# 6) Iterative Token Reduction — three staged versions; you can return all or just the most compressed
import re

def iterative_token_reduction(document: str, return_stage: str = "final") -> str:
    """
    return_stage: "all" -> V1/V2/V3, "final" -> V3 only
    """
    prompt = f"""
Perform ITERATIVE TOKEN REDUCTION in one pass.

Produce three increasingly compressed versions:
  V1: ≈50% of original length
  V2: ≈30% of original length
  V3: ≈15% of original length (most compressed)

Requirements:
- Preserve key entities, numbers, and causal relations.
- Each version MUST be strictly shorter than the previous.
- Plain text, prefix each section exactly with 'V1:', 'V2:', 'V3:' (one per line/section).

DOCUMENT:
{document}
"""
    resp = model.generate_content(prompt)
    text = (resp.text or "").strip()

    if return_stage.lower() == "all":
        return text

    # Return V3 only
    m = re.search(r"(?is)^\s*V3:\s*(.*)$", text)
    return m.group(1).strip() if m else text