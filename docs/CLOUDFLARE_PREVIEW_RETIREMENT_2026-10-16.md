# No-credit-card preview review and retirement proposal

Status: `REVIEW_PENDING_CHATGPT`. Inspection only; no provider setting or deployment was changed. Zero Trust billing onboarding is stopped. No payment information was entered, no plan or overage consent was accepted, and no new subscription, paid feature, Worker, recurring job, credential, or deployment was created. No pushes, PR writes, merges, DNS, or DOT actions occurred. Local implementation commits and previous reports remain intact.

This supersedes any earlier suggestion to complete Zero Trust enrollment. The owner's current requirement is local development, no new payment method, no new recurring charges, and no uncapped spending authorization. An existing account payment method and annual registrar renewals were observed in the previous billing review; this task neither removes nor changes them. A claim that the whole existing account has no payment method would be false. No-card preview work must not be confused with changing those existing registrar arrangements.

## Verified current protection and limits

At 2026-10-16T17:02:31.940Z, cookie-free HTTPS GETs with redirects disabled checked all 38 hosted preview URLs and both branch aliases. All 40 returned HTTP 302 to the existing Cloudflare Access login domain, with only a small redirect body, not website content. Five production URLs returned HTTP 200 and their website titles: `cajun-ai-production.pages.dev`, `tradeboard-website.pages.dev`, `cajun-ai.com`, `www.cajun-ai.com`, and `trade-board.net`.

The two existing Access applications were re-read: each protects only `*.<project>.pages.dev`, with one Allow Members email rule matching the signed-in owner, and no bypass/Everyone rule. Policy IDs and destination details are in the main website validation report. Production roots and custom domains are not included. Cloudflare One Settings still says no plan has been chosen and warns of possible disruptions. This is a real anonymous-denial PASS **now**, not a certified ongoing no-card Access service. Authenticated owner access, non-owner authenticated rejection, and future Access availability remain NOT VERIFIED. This review intentionally did not resume email-code login or billing setup.

Both branch-control dialogs were inspected without saving: production `main`, automatic production deployments enabled, preview Custom branches, include `*`, exclude exact `marketing/20261016-release-truth`. The `None (Disable automatic branch deployments)` option exists. It is **not selected or applied** by this task.

## No-credit-card options and exact recommendation

| Option | Verified behavior / security implication | Recommendation |
| --- | --- | --- |
| Local builds and browser tests on loopback only | No new cloud deployment or billing enrollment; keep dev servers bound to loopback and use synthetic/redacted data | Preferred development workflow; no tunnels or new hosting services |
| Preview branches = None on both projects | Existing dashboard offers this without checkout; official docs say it stops automatic preview builds. It does not revoke old hashes, stop manual deployments, or change production automatic deployments | Prepare now; apply only after owner approves the settings change |
| Retain existing Access, no enrollment | All 40 preview endpoints deny anonymous website content now; no ongoing availability guarantee because no plan is selected | Preserve as the current guard; do not disable/delete the applications or broaden policies |
| Retire published preview artifacts | Removes hosted review copies rather than relying on a billing-dependent login flow; deletion loses the hosted artifact/history and requires explicit approval | Propose exact Preview-only UUID allowlist below; never delete a project or Production record |

Exact proposed settings operation for **each** of `cajun-ai-production` and `tradeboard-website`: Workers & Pages > project > Settings > Build > Branch control > Edit; select `None (Disable automatic branch deployments)` under Preview branch; keep Production branch `main` and the checked `Enable automatic production branch deployments` box unchanged; Save. Reopen and verify None, main, and the unchanged checkbox. Keep Preview access restricted. Do not disconnect GitHub, alter production controls, DNS/custom domains, builds, runtime, bindings, or billing. Expected incremental recurring fee for this setting is $0; it creates no service or resource and consumes no build allowance. A test push/build is neither needed nor authorized.

## Safe retirement proposal — not executed

1. First obtain approval for the reversible None setting and apply/read it back. No manual preview build is proposed.
2. Preserve all local commits/reports and re-read live project/environment/UUID/alias before any approved deletion. The inventory below is an explicit list, not authorization. If history has changed, stop and reconcile it.
3. There are 36 older hosted previews (29 Cajun AI, 7 TradeBoard) without the current branch alias, plus two current aliased previews. Older artifacts are the first retirement candidates after owner approval; skip 21 records with no hosted artifact. Preserve all 27 Production history records, including both current production UUIDs, without exception.
4. Dashboard deployment details expose Manage deployment > Delete deployment (observed on the latest TradeBoard preview), but Delete was not clicked and no deletion behavior was tested. Use an approved, exact Preview UUID, never project deletion or a broad age-based sweep. Keep Access in place throughout. After each approved deletion, request that hash without cookies and require unavailable content (normally 404), not a different preview. An Access redirect alone does not prove deletion; also verify the record is removed from the dashboard. Recheck public production after a bounded batch.
5. Current aliased previews need special handling. The [current API reference](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/delete/) documents `force` for a **non-production** deployment with an active alias, and [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/pages/#deployment-delete) documents alias-aware deletion. However, the [Pages preview guide](https://developers.cloudflare.com/pages/configuration/preview-deployments/#delete-preview-deployments) still says the latest branch deployment cannot be deleted. This discrepancy is unresolved; do not promise that all aliases can be retired. Obtain owner approval and clarify provider-supported behavior before attempting either current aliased UUID. Do not deploy a blank replacement, change production, or remove Access to work around it.
6. After any future approved full preview retirement, verify every old hash and both aliases no longer serve review material and production remains public. Keep Access until this is proven, including direct asset/document routes where applicable. Deleting artifacts cannot revoke any copies downloaded while they were previously public. Public GitHub repositories also remain separate from hosting Access; do not push private material.

The exact two aliased UUIDs requiring separate handling are Cajun `d51eb552-a473-4eb9-8c62-fe6ecc6a6e27` and TradeBoard `e03944ca-435d-42e8-859f-153938d8bb75`. Both aliases are `marketing-20261016-release-t.<project>.pages.dev`; both were directly tested. Do not remove Access to avoid onboarding. No verified ongoing no-card hosted authentication alternative has been established; local-only review plus approved preview retirement is the preferred path.

Reference: [branch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/) describe None; [preview aliases](https://developers.cloudflare.com/pages/configuration/preview-deployments/#preview-aliases) explain why older hash URLs persist. `noindex`, browser storage flags, or removing a navigation link are not authentication or artifact retirement.

## Tests and evidence

- PASS: all seven dashboard history pages inventoried (Cajun 5, TradeBoard 2); 62 + 24 unique records reconciled with displayed totals. A transient pagination snapshot retained old rows; deduplication exposed it, and the missing page was re-read before accepting the inventory.
- PASS: 38 historical preview hash URLs + 2 aliases returned Access redirects; no billing completion was performed.
- PASS: 5 production roots/custom domains returned public 200 responses.
- PASS: both Access applications and exact owner-email rules re-read; both current branch-control dialogs inspected, then canceled.
- NOT VERIFIED / not run: actual None save, any deletion, post-deletion behavior, alias-aware forced deletion, owner authentication, ongoing Access availability or guaranteed $0 cap for enrollment.
- Local raw evidence: `C:/webull-dashboard/.website-review/qa/cloudflare-deployment-inventory-2026-10-16.json`, `historical-preview-access-results-2026-10-16.json`, and `check-historical-previews.cjs`. Query strings with transient Access metadata are omitted. No authentication secrets or account payment details are included in this report.

## Complete inventory for `cajun-ai-production`

62 records: 30 hosted previews, 19 skipped/no-artifact preview records, 13 Production records. All Preview records use `marketing/20261016-release-truth`. Current production UUID: `8896466a-be82-4698-9ad2-202de6be9e01`.

### Hosted previews

| Full deployment UUID | URL | Source commit | Current anonymous test | Retirement proposal |
| --- | --- | --- | --- | --- |
| `d51eb552-a473-4eb9-8c62-fe6ecc6a6e27` | https://d51eb552.cajun-ai-production.pages.dev | `2e295e128c3279d6c2e1687de797a7ff4b728da4` | PASS: 302 to Access | HOLD: current branch alias; provider/owner handling required |
| `5246abdd-f8b4-4d43-a549-888e50c6c3f9` | https://5246abdd.cajun-ai-production.pages.dev | `0798a3f63b2745ac98a764b9687aaca59e721d02` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `ff9170c6-20e7-4e0e-8cc8-9c690c0b2e22` | https://ff9170c6.cajun-ai-production.pages.dev | `2bac88e2262fd117e7d984e8a9b207aad24a3552` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `275014f4-208c-4ba2-8dcb-4687efd97030` | https://275014f4.cajun-ai-production.pages.dev | `4c36f63f72316918024f445c9c3e27fcfceb6c1c` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `40c6102e-9c18-4cd4-a608-762aee98b45c` | https://40c6102e.cajun-ai-production.pages.dev | `4079ea9c469056d3761fa8f012d0a7d8e1eb1769` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `fb6a418d-44a5-4a3e-aebe-e764292f57a8` | https://fb6a418d.cajun-ai-production.pages.dev | `f3293c0ecc291627409d8fa853782c26734b5504` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `81ad91ae-83ef-4e33-921a-d9723eb3def5` | https://81ad91ae.cajun-ai-production.pages.dev | `356e944ce526bde05243f0b06a95fada2857f1f0` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `24f75b25-5bb5-4feb-8cc8-c04a85670443` | https://24f75b25.cajun-ai-production.pages.dev | `12cc537c042aec215e808d490cf3f3e9ba843ad4` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `2277ab9d-5393-44aa-a874-86df9d36d874` | https://2277ab9d.cajun-ai-production.pages.dev | `993351a18be98d807fd3511c34194670610981a6` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `ab1dbfca-9160-4c56-b209-2c272190c6a2` | https://ab1dbfca.cajun-ai-production.pages.dev | `d7d14b50781e199aac07c353f8275926b1878362` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `47eac042-87d8-4718-ac8b-07bb4881799e` | https://47eac042.cajun-ai-production.pages.dev | `6f99d05a6614fc99f90a48bf4108f615de4d4c87` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `23ae94e3-63e2-4cee-9c09-484172b9c729` | https://23ae94e3.cajun-ai-production.pages.dev | `c7719797927245c0bb63430a5d03b341a0cc182b` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `47581220-b10e-4f66-ac9e-180a54f58b88` | https://47581220.cajun-ai-production.pages.dev | `1e169b53712b8d9cab257f39b488b8ce39bdf823` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `244a4ef7-fbc6-4b68-b038-e7849f1e9a28` | https://244a4ef7.cajun-ai-production.pages.dev | `e139168ff081befce9354b40850214a1a47eee20` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `3d6ec09d-c2c0-456a-b76d-e0399d98e266` | https://3d6ec09d.cajun-ai-production.pages.dev | `83d9059fea9d02d0568cdb243c4065bc1ab79acd` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `3e03b1a3-a447-48ab-b1dd-4d747a42d1a3` | https://3e03b1a3.cajun-ai-production.pages.dev | `8d8a1d5c89bb4607d5568784178fea9f1fa83780` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `3e19b1ef-ea6f-442a-8877-32a2425a1738` | https://3e19b1ef.cajun-ai-production.pages.dev | `6188224fda8f421aecb813c5614ff4602ad8fc21` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `9bfaf86e-581e-4952-89df-f299d3e88d3f` | https://9bfaf86e.cajun-ai-production.pages.dev | `1934b8563c1a6e6a9dbf4ad10f36e28bd8c7710f` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `de172825-23bb-4f66-8a49-74d54494b3a5` | https://de172825.cajun-ai-production.pages.dev | `62b34cca98af9167ebb50997a4697bc71181ee41` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `5c69e6e8-3e8a-4ee0-a001-06f6ccebc4e1` | https://5c69e6e8.cajun-ai-production.pages.dev | `e6ca396310ff70f683032eb039df182c4bf01ddd` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `f7951e55-493b-43c4-9281-9448f30d9d6c` | https://f7951e55.cajun-ai-production.pages.dev | `f5d28373590cc140da77036bc073e6359a12dd36` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `65d1e840-ec1b-4251-a5b8-ad99a80b398c` | https://65d1e840.cajun-ai-production.pages.dev | `15d3204d2890c5d3297d3302b63a1ad55fc87bde` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `2182dcd6-e545-4e9d-9cb0-9bac99cdfa93` | https://2182dcd6.cajun-ai-production.pages.dev | `bfe7580c7b6d57fff248f9dbef40adf1607345f2` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `a86b73cd-218d-49b9-ac1b-d8ed2c4c0d6f` | https://a86b73cd.cajun-ai-production.pages.dev | `5ed96b5b2249f885e5a0965de574584c645862d4` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `5c0d81d3-2caf-4fc2-8a55-56c28c895f41` | https://5c0d81d3.cajun-ai-production.pages.dev | `406b39b9207f746e53e38e377f4496159c990826` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `814e1418-418e-4fcd-b407-d2c313bc1df8` | https://814e1418.cajun-ai-production.pages.dev | `fd71eafef7fad8d4f9a7d2fc40a41d6bfb740662` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `426e4515-4dae-4a4f-be64-795129d7f75d` | https://426e4515.cajun-ai-production.pages.dev | `fb87d6938430e341717a35300a97fe2629e7cc43` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `3a3b356d-5eb0-4a0e-ad46-df3e47a98f9e` | https://3a3b356d.cajun-ai-production.pages.dev | `f963c16b1b22b643ada49d29edba93637ed4acaa` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `7d356223-4326-4aa3-b0bb-79779d2700bb` | https://7d356223.cajun-ai-production.pages.dev | `d3fa059426032b97111cd65bb6d399b613e976cd` | PASS: 302 to Access | Older candidate; delete only after explicit approval |
| `a80596f2-28c2-4db2-8ca7-99f892dad7a5` | https://a80596f2.cajun-ai-production.pages.dev | `66e49c49b851fcfa9fa5a510ced483714eb3822d` | PASS: 302 to Access | Older candidate; delete only after explicit approval |

### Skipped preview records — no hosted URL listed

- `b8e971b3-07a0-4c21-9f6e-8e0e2da2df0d` — source `c85cfdb77db0931d0a5ccdaf10852e16693e12af`; no artifact listed, not proposed for deletion.
- `f8d66df9-257c-4e12-8154-6d78def204a6` — source `d1677c23c8d5b373091e63b5626d78238e084004`; no artifact listed, not proposed for deletion.
- `65ee3e09-9b76-408e-93e7-9d47d931d8fe` — source `8ec8151a99a5ab12fc481d867e59d6d44effaba6`; no artifact listed, not proposed for deletion.
- `57111e7b-3b01-4183-90d7-b395fec116a6` — source `b905af7f270e016cc1b168076788a2330fc6888c`; no artifact listed, not proposed for deletion.
- `b92fbdc5-7c4a-4f35-8596-d5b705ece13d` — source `f5adf66f4487c29490065752098385a1f95fe90b`; no artifact listed, not proposed for deletion.
- `9cee3c9c-6d95-4684-bb44-91884c03a7a7` — source `df9d4826dd11afce0966b6445779e81edba02e62`; no artifact listed, not proposed for deletion.
- `b90f61f3-0618-46f4-965f-5170db2bfff5` — source `9d5705e9d7b25a8ee8eb7e9fa78fea0000c2f3d7`; no artifact listed, not proposed for deletion.
- `31cf6e8a-151a-48f5-9a0d-6c6215507d2d` — source `c21685b5961a8d9f6963b080d9a79bab6233c3e3`; no artifact listed, not proposed for deletion.
- `e684c7c3-0b5f-47dc-9173-0c31a9eb3835` — source `49bb13cc0c9d8edad5edf7744d4bd3c9921fc0a2`; no artifact listed, not proposed for deletion.
- `20f9422b-acd2-4230-9419-c311c94ee124` — source `83ec8de9ae96731efcf9ba059bed986b8a5734a4`; no artifact listed, not proposed for deletion.
- `d70dceca-c307-4976-93eb-e13e176b5225` — source `910a40095ee94f818713c1a8c9ce54c59feeea9b`; no artifact listed, not proposed for deletion.
- `9654ca86-78b7-4e9a-9b41-484f3b04c6f6` — source `7a491b760f1c92f1ac008dea802dda8295ea4eb2`; no artifact listed, not proposed for deletion.
- `6e7af679-fca0-4e5d-a51e-4b53bd70dd83` — source `bb6e92da99ff5d24c019a5edfac3ce7eae0899d2`; no artifact listed, not proposed for deletion.
- `b8d6e215-20c0-4e29-aace-5461c0c7f1e9` — source `4d06e28e0be5e03f203c6b8e55f31fb7e943b10c`; no artifact listed, not proposed for deletion.
- `4d5b4d6c-19d1-4b06-8f66-44fadcac678c` — source `3df60be51262622379ea104c7a3ed499189e84dd`; no artifact listed, not proposed for deletion.
- `c569d5e1-085e-4932-b8ba-1a177d2152e3` — source `e15e8e660775d7ed11602cfc5d8b4d222cb01d14`; no artifact listed, not proposed for deletion.
- `1dd1f534-ae3b-4c47-b949-5fec4904badb` — source `c26df3cb36dd50c6f3ed790b144dcbdcd38f4625`; no artifact listed, not proposed for deletion.
- `df03ce91-7df2-474d-8267-4da26e4876db` — source `3e4e0226d3f2ef3740b217a964b348477d61ef22`; no artifact listed, not proposed for deletion.
- `653e6a5e-bb15-42ec-a929-9ce03ae429ff` — source `7321d89b96bdaadaa72f47ebe3b6a06999e4d599`; no artifact listed, not proposed for deletion.

### Production preservation list — never included in retirement

- `5fc4a8b3-4f76-472e-ba25-4a12a7741452` — `main`, source `2d34dd939f39afd8f18485f6616b112e03b47074`; PRESERVE.
- `f76272b1-17ee-4ed8-a9f9-a86d79779b48` — `main`, source `ad15c412eabf3f84432829553601025b5a1f53c0`; PRESERVE.
- `8896466a-be82-4698-9ad2-202de6be9e01` — `main`, source `66e49c49b851fcfa9fa5a510ced483714eb3822d`; PRESERVE.
- `81010b07-bd6b-490e-a9f8-de062047c605` — `main`, source `50011460132edfb7a2dd50a7e8788f5c98c18e27`; PRESERVE.
- `a6b92934-dbf6-4089-a8f3-a3d55cd97df7` — `main`, source `4296f9a8df08c6cf80670c13152495ed01353a84`; PRESERVE.
- `770cfd1f-f1b1-48a4-82f0-e7c84f8e4788` — `main`, source `e2e4091e281a40a186070cf93de213e25f7d0f4a`; PRESERVE.
- `65371cd6-74ab-45cb-8ba0-dd360a1cb63a` — `main`, source `f19dd0d509005c7945ad382163fd793bae6e4bf2`; PRESERVE.
- `4c294b8d-d73a-4cd8-a21e-51d79aa7c5b9` — `main`, source `26461f9e5fc82a954846d9baee0a9178a7c65e2c`; PRESERVE.
- `9607a6d7-c8db-4703-9366-09315785c135` — `main`, source `3f02c333f041a431afb68adb65e736666e6b2429`; PRESERVE.
- `6f2f474c-b22f-4a95-9681-3501e4c1a710` — `main`, source `ad7c97b40210ce704e86e23345c87ea8cb5f7ed8`; PRESERVE.
- `b5ce63a3-4fb9-40ff-923a-28016e8b50f7` — `main`, source `37f145f20e56a77b07be792f33708d7e8dfc4156`; PRESERVE.
- `73571281-0e0b-40fa-907f-bad6d629a906` — `main`, source `34fbd4a96b233c9afb909db79d4967eb132107fe`; PRESERVE.
- `5409f813-6447-40e2-b809-1867d479cb3d` — `main`, source `e9af6528aba1249e4b622d4a3321157693e33f62`; PRESERVE.


## Subsequent approved None-setting completion

The owner subsequently authorized only automatic preview disablement. Both projects now persist Preview branch deployments = None, production main and automatic production deployments enabled. Three production custom domains remain Active/SSL enabled and publicly accessible. All 38 historical preview hash URLs and both aliases still return Access redirects. History totals remain 62/24; no deployment was deleted and no Access policy or billing setting was changed. The earlier inventory/retirement proposal remains historical and confers no deletion authorization. See the final owner-approved automatic preview disablement section of [the main validation report](WEBSITE_RELEASE_VALIDATION_2026-10-16.md) for exact before/after settings and test times. `REVIEW_PENDING_CHATGPT`.
