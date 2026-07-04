# CLRTY-1 Market Launch and Exchange Listing 100-Task Checklist

This document converts the market-launch checklist into a CLRTY-1 specific evidence tracker for exchange listing, market launch, and institutional readiness.

Canonical security policy:

```text
https://github.com/clarity-fintech/security/blob/main/SECURITY.md
```

CLRTY-1 stress evidence:

```text
https://github.com/clarity-fintech/security/blob/main/docs/CLRTY1_LIVE_CHAIN_STRESS_REPORT.md
```

## CLRTY-1 Launch Position

| Field | Value |
|-------|-------|
| Asset | CLRTY |
| Chain | `clrty-1` |
| Denom | `uclrty` |
| Asset type | Native L1 |
| Decimals | `9` |
| Max supply | `16,000,000 CLRTY` |
| Public contract address | Not publicly disclosed; no public wrapped-token contract is claimed |
| ERC-20 / SPL mirrors | Deferred until bridge or wrapped-token deployment |
| Latest local/simulated stress result | PASS: 8/8 checks, L-DNET 50/50 |

Statuses:

| Status | Meaning |
|--------|---------|
| Active | Public repository process, policy, or artifact exists. |
| Evidence attached | In-repo evidence or generated stress output exists. |
| Evidence required | Work may be designed, but proof must be attached before claiming completion. |
| External attestation required | Requires counsel, auditor, SOC 2, market maker, exchange, or vendor confirmation. |
| Deferred | Not in the current L1 launch scope. |

## Pillar 1: Source Code and Smart Contract Security (1-20)

| ID | Task | CLRTY-1 treatment | Status |
|----|------|-------------------|--------|
| 1 | Architecture design | Maintain protocol, chain, security, and technical architecture docs for `clrty-1`. | Active |
| 2 | Environment setup | Rust workspace, CLI, substrate modules, stress scripts, and local test commands are present. | Active |
| 3 | Core logic implementation | Native L1 logic is implemented across `CLRTY_SUBSTRATE`, CLI, API, settlement, and runtime modules. | Evidence required |
| 4 | Standard compliance | Native `uclrty` is authoritative at launch; ERC-20/SPL compatibility applies only to future wrapped mirrors. | Deferred |
| 5 | Access controls | Governance, signer, treasury, and admin controls must remain multisig/timelock governed. | Evidence required |
| 6 | Gas optimization | Native L1 execution cost and deferred EVM mirror gas profiles require separate evidence. | Evidence required |
| 7 | Unit testing | Rust unit and integration tests run as part of the CLRTY-1 stress battery. | Evidence attached |
| 8 | Code coverage | Coverage target remains 100% for critical launch modules; coverage report still required. | Evidence required |
| 9 | Static analysis | Rust audits plus EVM tools such as Slither/Mythril are required for wrapped-token contracts when activated. | Evidence required |
| 10 | Dynamic testing | Local and simulated chain tests executed for genesis, L-DNET, fuzz, nano, bridge audit, arbitrage, and fork-swap checks. | Evidence attached |
| 11 | Check-effects-interactions | Required for EVM/wrapped contracts and settlement-adjacent logic. | Evidence required |
| 12 | Arithmetic safety | Native supply checks and arithmetic invariants are verified through genesis and stress tests. | Evidence attached |
| 13 | Dependency audit | Dependency and lockfile scans must be attached before final listing. | Evidence required |
| 14 | Documentation | Security policy, exchange readiness, live-chain stress report, and Notion tracker are public. | Active |
| 15 | Private key strategy | Multisig/HSM/hardware signer architecture is required for treasury, admin, and deployer keys. | Evidence required |
| 16 | Upgradeability plan | Native runtime and future mirror upgrade paths must be documented and timelocked where mutable. | Evidence required |
| 17 | Pre-audit code freeze | Code freeze manifest and audit scope must be pinned before external review. | Evidence required |
| 18 | External audit round 1 | Third-party auditor must review launch-critical code. | External attestation required |
| 19 | Audit remediation | Finding-by-finding remediation matrix required after audit. | External attestation required |
| 20 | Final audit report | Clean final audit certificate or published report required for top-tier listing claims. | External attestation required |

## Pillar 2: Blockchain Management and Mainnet Simulation (21-40)

| ID | Task | CLRTY-1 treatment | Status |
|----|------|-------------------|--------|
| 21 | Testnet deployment | Public testnet or staging deployment evidence required before hosted-mainnet claims. | Evidence required |
| 22 | Faucet setup | Clarity Fortress faucet and testnet distribution process require live endpoint evidence. | Evidence required |
| 23 | Cross-chain testing | Bridge and wrapped-token functionality are deferred from L1 launch. | Deferred |
| 24 | Node configuration | Validator, sentry, RPC, and node configuration docs exist; production SLA evidence still required. | Evidence required |
| 25 | Network monitoring | Monitoring and alerting must attach dashboard/alert evidence. | Evidence required |
| 26 | Fork scenarios | Bounded fork-swap stress executed locally for 25 iterations. | Evidence attached |
| 27 | Stress testing | Local/simulated stress battery passed 8/8 checks, including L-DNET 50/50 and 50 simulated blocks. | Evidence attached |
| 28 | Edge case analysis | Fuzz, nano, arbitrage, bridge audit, and fork-swap checks ran successfully. | Evidence attached |
| 29 | API performance | Hosted RPC/API saturation test needs configured endpoint, rate limit, and operator approval. | Evidence required |
| 30 | Finality verification | Finality assumptions and deposit-crediting rules require production validator/RPC evidence. | Evidence required |
| 31 | Explorer integration | Explorer metadata and indexer verification required for exchange integration. | Evidence required |
| 32 | Mainnet dry run | Full staging mainnet dry run remains a launch gate. | Evidence required |
| 33 | Recovery drills | Node/database restore and stuck-asset recovery drills required. | Evidence required |
| 34 | Gas estimation accuracy | Applies to wallet and deferred EVM mirror flows; native fee estimation evidence required. | Evidence required |
| 35 | Wallet compatibility | Native CLRTY-1 wallet metadata and supported wallet matrices required. | Evidence required |
| 36 | Emergency pause logic | Emergency pause/freeze/circuit-breaker controls must be documented and tested where applicable. | Evidence required |
| 37 | Upgradeability testing | Mock upgrade and rollback rehearsal required for mutable components. | Evidence required |
| 38 | Governance simulation | DAO/council/timelock simulation required before governance handoff. | Evidence required |
| 39 | State consistency | Genesis verification passed with deterministic checksum. | Evidence attached |
| 40 | Deployment automation | Repeatable CI/CD deployment and rollback pipeline evidence required. | Evidence required |

## Pillar 3: Exchange Readiness and Compliance (41-65)

| ID | Task | CLRTY-1 treatment | Status |
|----|------|-------------------|--------|
| 41 | Legal opinion letter | Counsel memo needed for token classification and jurisdictional treatment. | External attestation required |
| 42 | KYC/AML policy | Formal KYC/AML policy required for platform and exchange review. | External attestation required |
| 43 | Terms of service | Public legally vetted terms required. | Evidence required |
| 44 | Jurisdictional mapping | Restricted jurisdiction matrix and enforcement mechanism required. | External attestation required |
| 45 | Transparency documentation | Listing kit, whitepaper, stress report, security policy, and audit reports must be packaged. | Evidence required |
| 46 | Exchange tier selection | Target exchange tier and liquidity fit must be documented. | Evidence required |
| 47 | Application submission | Exchange applications require completed disclosure packet. | External attestation required |
| 48 | Technical integration | Exchange-facing API, node, deposit, withdrawal, and metadata docs required. | Evidence required |
| 49 | Custodial workflow | Deposit/withdrawal and custody workflow required for exchange ops. | External attestation required |
| 50 | Admin key renunciation | Final admin handoff or DAO control path must be executed and evidenced. | Evidence required |
| 51 | Sanctions filtering | Address/entity screening process required. | External attestation required |
| 52 | Risk disclosure | Public token/protocol risk disclosure required. | Evidence required |
| 53 | Contact points | 24/7 technical, security, compliance, and exchange liaison contacts required. | Operational readiness |
| 54 | Incident playbook | Post-incident exchange and public communication templates required. | Operational readiness |
| 55 | Market maker agreement | Executed agreement or provider confirmation required. | External attestation required |
| 56 | Liquidity depth targets | Bid/ask spread and depth KPIs required for launch pairs. | External attestation required |
| 57 | Incentive design | Liquidity/staking incentives must avoid wash-trading incentives. | Evidence required |
| 58 | Asset icon and metadata | CoinGecko, explorer, wallet, and listing metadata required. | Evidence required |
| 59 | Clearing/settlement | Clearing partner or settlement rails must be documented where applicable. | External attestation required |
| 60 | Reporting cadence | Treasury, development, and operational reporting cadence required. | Operational readiness |
| 61 | SOC 2 compliance | SOC 2 readiness or report required for institutional/custodial claims. | External attestation required |
| 62 | Data protection policy | GDPR/privacy/data protection policy required. | External attestation required |
| 63 | Emergency contact | DPO/security lead contact required. | Operational readiness |
| 64 | Listing fee budget | Listing and integration fee budget/escrow required. | External attestation required |
| 65 | Market maker coordination | Market maker testnet/native inventory and launch readiness must be verified. | External attestation required |

## Pillar 4: Liquidity and Market Genesis (66-85)

| ID | Task | CLRTY-1 treatment | Status |
|----|------|-------------------|--------|
| 66 | Initial offering strategy | IDO/IEO/self-hosted strategy must be finalized. | Evidence required |
| 67 | Liquidity seeding | Initial LP, CEX, or treasury liquidity plan required. | External attestation required |
| 68 | LP token locking | Applies to DEX pools or wrapped-token pools when deployed. | Deferred |
| 69 | Burn proofs | Publish burn transaction proofs if burns occur. | Evidence required |
| 70 | Arbitrage monitoring | Arbitrage core tests passed locally; production surveillance still required. | Evidence attached |
| 71 | Price discovery phase | Transfer-only, limit-only, and open-trading stages must be scheduled. | Operational readiness |
| 72 | CEX deposit opening | Exchange deposit timing must be coordinated. | External attestation required |
| 73 | Trading commencement | Global go-live time and comms plan required. | Operational readiness |
| 74 | Order book surveillance | Abnormal volume, manipulation, and spread monitoring required. | Operational readiness |
| 75 | Liquidity depth maintenance | Market maker coverage for first 48 hours required. | External attestation required |
| 76 | Incentivized staking | Rewards program must be validated mathematically and operationally. | Evidence required |
| 77 | API gateway | Public price/volume APIs require hosted availability and performance evidence. | Evidence required |
| 78 | Aggregator updates | DexScreener, DefiLlama, RootData, CoinGecko, and listing-platform data must be verified where applicable. | Evidence required |
| 79 | Cross-chain bridge liquidity | Deferred until bridge/wrapped-token activation. | Deferred |
| 80 | Node rewards | Validator/node reward distribution must be monitored after activation. | Evidence required |
| 81 | Conversion tracking | Exchange-to-dApp onboarding funnel tracking required. | Evidence required |
| 82 | Latency tuning | Real endpoint p95/p99 and saturation evidence required after endpoint approval. | Evidence required |
| 83 | Treasury management | Surplus liquidity movement to multisig-controlled vaults required. | Evidence required |
| 84 | Automated alerts | Treasury, LP wallet, node, RPC, and abnormal-flow alerts required. | Operational readiness |
| 85 | Feedback loop | Public security reporting and community bug-report process exists; broader support loop required. | Active |

## Pillar 5: Long-Term Operations (86-100)

| ID | Task | CLRTY-1 treatment | Status |
|----|------|-------------------|--------|
| 86 | Community governance | Inaugural DAO/council vote and governance handoff required. | Evidence required |
| 87 | Quarterly reporting | Automated financial and operational reporting process required. | Operational readiness |
| 88 | Security patch management | Fast-track emergency patch and disclosure process required. | Operational readiness |
| 89 | Bug bounty program | Public coordinated disclosure program exists; paid bounty platform optional/future. | Active |
| 90 | Roadmap updates | Post-launch milestone updates required. | Operational readiness |
| 91 | Retention programs | Ongoing liquidity and holder retention programs required. | Evidence required |
| 92 | Institutional onboarding | API access, docs, and support path for quant/institutional traders required. | Evidence required |
| 93 | Cross-platform integration | New ecosystem or L2 expansion is deferred beyond native L1 launch. | Deferred |
| 94 | Partner audits | Periodic platform integration audits required. | Operational readiness |
| 95 | Talent pipeline | Long-term protocol maintenance ownership required. | Operational readiness |
| 96 | Scaling strategy | Future scaling, bridge, L2, or sharding research must be maintained. | Evidence required |
| 97 | Global marketing alignment | Regional/channel launch messaging coordination required. | Operational readiness |
| 98 | Contingency fund | Emergency reserve in stable assets required. | External attestation required |
| 99 | Evolutionary planning | Research track for the next CLRTY iteration required. | Evidence required |
| 100 | Final operational review | Post-launch lessons-learned review required. | Operational readiness |

## Current Evidence Snapshot

The latest CLRTY-1 local/simulated evidence battery passed:

```text
overall_status=pass
passed=8
failed=0
total=8
genesis_checksum=0xdf3f767fecd60974c517d954ed0e28b92728c21b507dc54139025f09075f2e61
ldnet=50/50
```

The remaining major gate is hosted live endpoint testing. No configured `CLRTY_API_URL`, `CLRTY_API_BASE`, or `CLRTY_L1_RPC` HTTP endpoint was present during the latest run, so hosted RPC saturation, validator SLA, explorer latency, and public-node p95/p99 evidence still require an approved endpoint and rate limit.
