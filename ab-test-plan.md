# A/B Test Plan: LeaseLens Iowa City

Author: Mick Delea
Plan written: 9 November 2026 (committed before any data collection)

## 1. Page and element being changed

**Page:** Homepage (index.html)
**Element:** The main headline (the H1) in the hero section. Nothing else changes.

- **Version A (current):** "Find an Iowa City apartment you will actually like living in"
- **Version B (variant):** "Read what real student tenants say before you sign your lease"

Everything else on the page is identical: the intro paragraph, the button, the navigation, the notice, and all other sections.

**Why this element:** The headline is the first thing a visitor reads and it frames the whole offer. Version A promises an outcome (a place you will like). Version B names the mechanism (reviews from verified student tenants) and speaks to the fear of signing a bad lease. Students choosing apartments are making a risky, expensive decision, so I believe proof of what other tenants experienced may be a stronger hook than a general promise.

**Where the variant lives:** ab-variant-b.html. It carries `<meta name="robots" content="noindex, nofollow">` and a canonical tag pointing to index.html, and it is left out of sitemap.xml. This keeps it from competing with version A in search.

## 2. Hypothesis

**Prediction:** Version B will produce a higher share of "yes" answers than version A, by at least 10 percentage points.

**Reasoning:** College students renting for the first time worry most about noise, maintenance, and landlords who do not respond. A headline that says reviews come from real tenants speaks to that worry directly and signals the product is trustworthy. A vague benefit like "an apartment you will like" is something every listing site claims.

**This could turn out wrong.** Version A may be clearer about what the app does, and B may feel like a mere feature description. A flat or reversed result would count against my hypothesis.

## 3. Method

**Visitor:** An AI model playing a college student. Every trial is run in a brand-new conversation with no memory of earlier trials.

**Model and settings:** Claude Sonnet 5.5 (claude.ai chat), default settings, new chat for every trial. The model is not switched during the test.

**Persona and task (identical in every trial, word for word, except for the page text):**

> You are a 20-year-old University of Iowa student who needs to find an apartment in Iowa City for next school year. You have a limited budget and you share the place with roommates. You are browsing the web and land on the page below. Read it and decide whether you would sign up for or download this app. Answer "yes" or "no" on the first line, then give one sentence of reasoning.
>
> PAGE:
> [full text of the homepage, version A or version B]

**How the page is shown:** As the full page text, pasted into the prompt the same way in every trial.

**Assignment:** Before running anything, I will generate a list of 120 assignments in Python: 60 A and 60 B, shuffled with `random.shuffle` using a recorded seed (seed: 4417). The list is saved as assignments.csv and committed before the first trial. Trials are run in the order of the list. I do not choose any assignment myself.

## 4. Primary outcome

**One outcome:** The yes/no answer to "would you sign up for or download this app?" Yes = 1, No = 0.

The one-sentence reasoning is recorded for every trial but is not used as an outcome.

## 5. Sample size and timing

- **Trials per version:** 60 (120 total).
- **Stopping rule:** I will run all 120 trials and not stop early or look at results partway.
- **Dates:** Launch on or before 12 November 2026. All trials complete by 17 November 2026.
- **Exclusions:** None planned. If a trial fails for a technical reason (for example, an error or an empty reply), I will log it with the date and rerun it with the same assignment. I will not drop trials because of their content.

## 6. Analysis and decision rule

- Compare the yes-rate in A with the yes-rate in B.
- Report the difference in percentage points and a 95% confidence interval.
- Test with a two-proportion z-test (and Fisher's exact test as a check), two-sided, alpha = 0.05.

**Supports my hypothesis:** B's yes-rate is higher than A's by at least 10 points AND p < 0.05.
**Does not support it:** Any other result, including a higher B rate that is not statistically significant. I will report it as inconclusive, not as a win.

**Known limits:** With 60 trials per version, the test can only reliably detect a large difference (roughly 25 points or more). A real but small effect would likely be missed. AI visitors also cannot tell me how real students behave, so a result would be a hint about message clarity, not proof of real-world conversion.

## 7. Changes after launch

Any change to the plan, pages, prompt, or model after the first trial will be logged in the report with the date and the reason.
