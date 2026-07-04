# CLRTY-1 Live Chain Stress Report

Generated from the current CLRTY repository state and locally available chain data on 2026-07-04.

## Scope

This report covers the live-version CLRTY asset model and the CLRTY-1 blockchain readiness surface using non-destructive local/simulated chain tests.

| Field | Value |
|-------|-------|
| Asset | CLRTY |
| Asset kind | Native L1 |
| Chain | `clrty-1` |
| Denom | `uclrty` |
| Decimals | `9` |
| Max supply | `16,000,000 CLRTY` |
| Contract address | Not publicly disclosed; CLRTY is represented as native `uclrty` on `clrty-1` |
| Evidence summary | `var/compliance/clrty1_live_chain_stress_summary.json` |
| Evidence directory | `var/compliance/clrty1_live_chain_stress_20260704T143036Z` |
| Endpoint probe | `var/compliance/clrty1_live_endpoint_probe.json` |

## Result

Overall status: **PASS** for the available local/simulated CLRTY-1 chain battery.

| Check | Result | Evidence |
|-------|--------|----------|
| Genesis verification | PASS | `genesis_verify.txt` |
| L-DNET 50-test WORM stress suite | PASS, 50/50 | `ldnet_stress_report.json` |
| Fuzz stress | PASS | `fuzz_stress.txt` |
| Nano stress | PASS | `nano_stress.txt` |
| Bridge connection audit | PASS | `bridge_connection_audit.txt` |
| Arbitrage core tests | PASS | `arbitrage_core.txt` |
| L1 concurrency simulation | PASS, 50 simulated blocks + OQ1 smoke | `l1_concurrency_50.txt` |
| Fork-swap bounded stress | PASS, 25 iterations | `fork_swap_stress_25.txt` |

## Key Chain Evidence

Genesis verification returned:

```text
node.genesis OK - chain=clrty-1 supply=16000000 denom=uclrty checksum=0xdf3f767fecd60974c517d954ed0e28b92728c21b507dc54139025f09075f2e61
```

L-DNET stress returned:

```text
passed=50
failed=0
total=50
errors_found=[]
worm_log=var/ldnet/stress_audit.wrm
```

Endpoint probing returned:

```text
configured_endpoints=0
reachable_probes=0
```

No configured `CLRTY_API_URL`, `CLRTY_API_BASE`, or `CLRTY_L1_RPC` HTTP endpoint was present in the loaded `.env`, so no public/live RPC pressure test was run. The executed battery is therefore a real repository-backed local/simulated blockchain stress test, not a hosted-mainnet throughput claim.

## Commands Executed

```bash
cargo run -q -p clarity-cli --bin clrty -- --plain node genesis-verify
cargo run -q -p clrty-substrate --bin l-dnet-stress -- --json
cargo test -p clrty-substrate --test fuzz_stress
cargo test -p clrty-substrate nano_stress
cargo test -p clrty-substrate bridge_connection_audit
cargo test -p arbitrage_core
bash scripts/stress/l1_concurrency.sh 50
bash scripts/stress/fork_swap_stress.sh 25
```

## Exchange Readiness Interpretation

The available data supports the following condensed CLRTY-1 status:

- CLRTY is modeled as a native L1 asset on `clrty-1`, denom `uclrty`, with fixed 16M supply and null mint/freeze authority in the authoritative manifests.
- The local genesis verification path passes and returns a deterministic supply checksum.
- The L-DNET WORM audit stress suite passes all 50 nano-section checks.
- Fuzz, nano, bridge-connection, arbitrage, bounded fork-swap, and concurrency simulations passed without detected structural failures.
- Hosted RPC capacity, validator SLA, public explorer latency, and production node high-concurrency limits still require a configured live endpoint and explicit load-test budget before claiming hosted-mainnet stress capacity.

## Next Live-Network Gate

Before representing CLRTY-1 as stress-tested on a hosted/live endpoint, run the same evidence pack with:

```bash
CLRTY_L1_RPC=<approved endpoint>
CLRTY_API_BASE=<approved endpoint>
```

and an explicit rate limit, duration, and allowlist from the node operator. Store the resulting RPC latency, error-rate, p95/p99, and saturation data alongside this report.
