# Case Study — Chapter 11: The SDK — Build vs. Buy
*The Cognition Economy — Dr. Ernesto Lee, 2026*

---

## Case Study: The Three Proposals at Cypress Coastal Insurance

### Background

Cypress Coastal Insurance is a regional property and casualty carrier headquartered in Tampa, Florida, with about five hundred employees and roughly $700 million in annual written premium. The firm serves Florida homeowners and small commercial property clients across Florida, Georgia, and Alabama, with a particular concentration in hurricane-exposed coastal counties. Chief Operating Officer Helena Vasquez initiated a strategic review of the firm's first-notice-of-loss (FNOL) process — the front-end claims workflow where every incoming claim gets reviewed, classified, and routed to an adjuster.

The numbers driving the review were straightforward. The firm receives roughly 9,000 FNOLs per year. Three claims analysts, working from a centralized intake queue, spend an average of two hours on each report before routing it. The work is heavy on document review — policy verification, coverage matching, anomaly flagging, and the writing of a one-page summary that goes to the assigned adjuster. The total annual labor allocation is approximately 18,000 hours, and Vasquez's analysis suggests that 60–70% of that work follows a pattern repetitive enough to be automated.

Vasquez assembled a small evaluation committee — Marcus Liang, the firm's senior software engineer; Priya Doshi, the Chief Compliance Officer; and Daniel Reyes, head of claims operations — to evaluate proposals. Three vendors were invited to pitch, and a no-code platform was added to the slate at Reyes's suggestion after he saw a competitor demonstration at an industry conference.

### The Situation

The first proposal came from ClaimsLogic AI, a venture-backed InsurTech vendor offering a fully managed claims pre-screening platform. Annual cost: $400,000. Implementation time: four months. Their pitch emphasized polish — pre-built integrations to common carrier systems, a slick analyst dashboard, vendor-managed model updates. The data tradeoff: FNOL documents would be transmitted to ClaimsLogic's cloud environment, processed there, and returned to Cypress as enriched outputs. Compliance officer Priya Doshi flagged this immediately. Florida insurance regulations and Cypress's reinsurance contracts impose data residency constraints that the ClaimsLogic architecture would only partially satisfy.

The second proposal came from Marcus Liang himself. His team, he argued, could build a custom claims pre-screening agent using the Claude Agent SDK, deployed inside Cypress's existing AWS environment. Estimated build cost: $80,000 for the first version, with ongoing operating costs of roughly $30,000 per year in API and infrastructure spend. Implementation time: four months. The agent would never send data outside the firm's own cloud account, would log every decision for audit purposes, and would be modifiable by Liang's small team as claims processes evolved. The tradeoff: Cypress would own the maintenance burden going forward, and Liang's team — three engineers total — would be the only people who fully understood the system.

The third proposal came from RelayWorks, a no-code agent platform that operations head Reyes had identified. Their proposal claimed to deploy a working FNOL pre-screening agent within a week, using a visual workflow builder that Reyes himself could maintain. Annual cost: $30,000. Data residency could be controlled through RelayWorks's enterprise tier, which kept all customer data within a dedicated tenant inside AWS. The tradeoff: less customization depth than a custom SDK build, and a platform dependency that worried Liang — what if RelayWorks raised prices, was acquired, or shut down?

Vasquez's challenge was not picking the cheapest option or the most polished demo. It was matching the architectural choice to the strategic position of the firm — its compliance posture, its engineering capacity, its competitive timeline, and its tolerance for vendor risk. Three internal stakeholders, three different recommendations, and a decision that would shape the firm's claims operations for the next five years.

### Discussion Prompt

Apply the four-question build-vs-buy framework from this chapter to Helena Vasquez's decision. Which option — vendor, custom SDK build, or no-code platform — best fits Cypress Coastal's profile, and what specific factors from the case lead you to that conclusion? Then take the opposite position and argue for one of the other two options. What would have to be true about Cypress's situation for the alternative path to be the correct choice? Finally, consider how Helena should sequence her decision: should she pick one path and commit, or run two paths in parallel to reduce risk, and what does the answer say about the broader leadership principle of "match the option to the shape of the problem"?

---

### Discussion Guidelines

**Initial Post** (due before class)
- Minimum **400 words**
- Directly address the discussion prompt using concepts from this chapter
- Include **at least one APA-formatted citation** — from the course text or a peer-reviewed source
- Avoid summary; demonstrate analysis and original thinking

**Peer Responses** (minimum 2)
- Minimum **250 words each**
- Each response must include **at least one APA-formatted citation**
- Engage substantively — build on, challenge, or offer a contrasting perspective grounded in evidence
- "I agree" or "Great post" responses do not meet the requirement
- Maintain a professional and respectful academic tone

---

