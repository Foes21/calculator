# Coursework evidence

Use these headings to organise your own results and explanations. Replace
bracketed prompts and remove unused prompts. Supplied headings are permitted
reuse; the evidence and explanation must be your own. Refer to short saved
logs rather than pasting entire CI logs.

Staff will not open your private GitHub repository. Save PR pages and CI
runs as PDFs or screenshots, with short log excerpts, in `evidence/` and
give their paths below alongside the URLs.

Complete and commit this file with your other documentation before the final
release checks. Record the final release hash, CI run and fresh-checkout outcome
in the separately submitted `SUBMISSION.txt`, outside the repository, and
submit the final CI run as a separate PDF or screenshot.

## 1. Starting point and Git review

- Starting commit: 86939b890b39e7b787a445ecfb0abed550070199

- Reused lab files, tests and examples: The four arithmetic functions, 
interactive mode, existing tests and workflow examples will all be continued 
from the progress made in the labs through weeks 1-5, and will be expanded upon
through both my own additions and additional lab work.

- Feature branch and PR: Most recent Pr - Broken multiplication; 
https://github.com/Foes20/calculator/pulls?q=is%3Apr - shown in InitialPulls.png

- Self-review: Before beginning with the new test cases, I checked the diff of the most recent 
commits, which displayed all changes made to the current state of the
calculator. From this, I determined that the additions I make through this 
coursework will allow a small file of calculations to be input, processed
and returned with the correct values.

## 2. Test failure, diagnosis and fix

Plan this before fixing the chosen missing requirement or defect. An initially
missing feature is acceptable; retain the test in the final suite.

- Requirement and retained test: R5/R7; Executing test_batch_calculator.py to 
ensure that batch_calculator.py is able to process data correctly, returning the
appropriate failure message or calculation outcome.

- Expected result and actual failure: When a valid operator and operand are 
entered, the values should be combined and returned to the function that called
batch_calculator. If invalid data is entered, an error should be returned 
instead. However, all entered data returns NotImplementedError, as the contents
of batch_calculator has not yet been written, thus always returns the same error.

- Before/fix commits: 
    Before commit: e70416f8c72c545012e2ecec9ad2a0cd9f0e7e17
    Fixed commit: 3af2479ddcd2d091b87fc17897afaf0404e01c80
    
- Failing/passing local runs:
    Failing local run: python3 -m pytest -v, returns NotImplementedError for each
    of the tests described in test_batch_calculator, with original calcualtor 
    tests still passing successfully; log details stored in
    evidence/local-before.txt
    Passing local run: python3 -m pytest -v, returns passed for each of the new 
    tests and the original tests; log details stored in
    evidence/local-after.txt
    
- Failing/passing CI runs:
    Failing CI run: https://github.com/Foes21/calculator/actions/runs/44952232475
    Commit e70416f, log details found in evidence/ci-before.txt and 
    evidence/ci-before.png
    Passing CI run: https://github.com/Foes21/calculator/actions/runs/45034118790
    Commit 3af2479, log details found in evidence/ci-after.txt and
    evidence/ci-before.png
    
- CI diagnosis: The event was initiated by attempting to push the contents of 
test_batch_runner and batch_runner to the coursework branch, along with the 
additional provided files, causing the new CI workflow to start. This executed on
a Linux platform using Python 3.11, and contained the tasks dictated through
ci.yml. Upon reaching the 'tests' phase, a failure occurred with each of the new 
tests in test_batch_calculator, returning the error message 
'NotImplementedError: Complete process_calculation for the coursework'

- Cause and implementation fix: By completing the contents of batch_calculator,
all of the operations were able to be performed correctly, including returning 
the appropriate error message, if the inputs were not valid. This allowed the 
assertions in test_batch_calculator to be marked as successful, thus allowing 
all tests to pass.

## 3. Repeatable checks and local hook

- Common check script: [path and invocation used locally and in CI]
- Prerequisites and hook installation: [commands or README reference]
- Blocked commit attempt: [short transcript, base commit and working-tree state]
- Permitted commit after the fix: [short transcript and resulting hash]
- Hook limitations and independent CI checks: [your explanation]

The hook may use the same failure case as section 2 or another case. A blocked
commit attempt has no new commit hash; identify its base commit and changes.

## 4. Native and container batch runs

- Native normal/mixed runs: [commands and saved output/diagnostic paths]
- Container build/run commands and image tag: [README reference or commands]
- Input/output transfer: [how files enter and leave the container]
- Mixed-run interpretation: [summary, one error and later successful records]
- Python version and Docker environment: [what you used]

## 5. Container checks in CI during development

- Checked-out source commit and CI run: [hash, URL and saved file in evidence/]
- Test gate, image build and smoke-test outcomes: [steps and results]
- Smoke fixture and expected-output check: [paths and what is asserted]
- Failure handling: [why failed tests stop the build and wrong output fails CI]

## 6. Reproduction notes

- Checkout tested during development: [commit]
- Documented setup and commands tried: [README reference]
- Outcome and any limitations: [your results]

The final fresh checkout must test the declared release commit. Record its
outcome in `SUBMISSION.txt` after the documentation is committed, CI passes
and the final commit is tagged. Do not create another commit just to insert
that commit's own hash or CI-run URL into this file.
