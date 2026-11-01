# Physical-phone test scope and cleanup

This scope was prepared before phone connection. Execution now includes retained
setup failures, verified owned-package removal, a small transport control and full
model byte verification. Those are setup evidence; native generation and repair
require their own completed receipts. The human authorized this scoped testing;
no broad device administration or warranty assurance is granted.

## Scope

The separate `:paperbench` module produces `com.example.aicontrolcentre.paperbench`
and its `.test` instrumentation package. Both packaged manifests have no requested
permissions or activity/service/receiver/provider components. Backup and cleartext
traffic are disabled. The original application ID and manifest are unchanged.
The coding agent receives only imported public repository copies and scoped file
tools; it receives no shell, settings, contacts, SMS, camera or media tools.
Native inference uses the existing pinned Gemma4 E2B artifact, CPU with two threads.
The model and all generated files live in private internal test-app storage.

Temporary instrumentation reads foreground package identity, memory, runtime and
test-model/tool journals. It does not export screenshots or user interface text.
Existing accessibility services are explicitly not suppressed by instrumentation.
No Accessibility Service, notification access, overlay, launcher or assistant role
is enabled. APK installation never grants runtime permissions.

## Device boundary

Use the exact authorized physical-device serial. Refuse either existing test
package instead of replacing it. Preflight requires reported stock verified boot,
locked bootloader and Knox0; unavailable state is a refusal, not an assurance.
No root, bootloader unlock, flashing, factory reset, firmware/kernel changes,
`settings`/`setprop` writes, system app removal, security bypass, reboot or CPU/GPU
overclock is part of these scripts. If a phone protection blocks ADB or installation,
stop rather than disable it.

USB debugging and the trust prompt are reversible choices made manually by the
human. ADB authorization is access to the phone; use only this trusted PC and revoke
that authorization/disable debugging after the test. Firmware remains untouched;
ordinary app installation necessarily creates normal package-manager records.

Before setup require thermal status below MODERATE, battery below40C and at least
25percent charge. During generation stop the owned app if status reaches MODERATE,
battery reaches45C or charge drops below25percent; unavailable sensors also stop
the test. These are conservative operational limits, not a guarantee against heat
or hardware faults. Every repository episode is limited to600seconds; native
initialization/cleanup are separately timed and are not assumed instantly preemptible.
Never force-stop an unrelated app. Public source copies are independently graded
on the host; no Python/shell/test runner executes in the phone agent.

October8 pre-execution amendment: after read-only39.7C/39.3C observations, the human
explicitly authorized starting at that temperature. The starting margin is now
below39.5C; the40C/MODERATE running stop and all phone protections remain unchanged.
The original38C protocol and source are retained. No phone assignment preceded
this amendment, which must be disclosed with its actual starting measurements.

Subsequent human instruction explicitly permits a45C ceiling. Before any native
inference, v5 records below40C starting and45C running limits; the MODERATE
thermal stop, low-charge/sensor stops and stock phone protections remain active.
Earlier source/protocol/failed setups are retained; no failed assignment is rerun.

## Cleanup commitment

After a completed or failed episode, collect research evidence to the PC, uninstall
only the two newly created test packages without `-k`, and query package presence
to verify removal. This removes the app-private model, repository copies, logs,
caches and exports. The session ownership receipt binds the exact serial and
fingerprint and refuses cleanup of existing/unrelated packages. Failed setup
attempts owned cleanup too. If a disconnect/crash prevents confirmation, record
cleanup as unverified and reconnect for the dedicated cleanup action; never say
cleanup completed merely because a command was attempted.

PC research code and measurement receipts remain for Kaggle reproducibility. This
scope does not delete the user's project or personal phone files. The user manually
revokes USB authorization and switches USB debugging off afterward. No phone
setting is silently changed or restored by guessing its original value.

## Execution entry points

Use `scripts/build_paperbench_checks.py` and its distinct APK/source binding.
Use `scripts/paperbench_phone_session.py prepare` for stock/health/package checks,
exclusive ownership, APK installation and private model staging. Use the isolated
`scripts/run_paperbench_repository_episode.py --session ...` for actual generation
and verified cleanup. The older full-application runner must not be used on this
phone for this request. The dedicated cleanup action is available if interrupted.
No installation or workload begins merely because a cable is attached; inspect
the authorized transport and device preflight first.

## Warranty and scientific limits

[Samsung Knox](https://docs.samsungknox.com/admin/fundamentals/whitepaper/samsung-knox-mobile-security/system-security/hw-backed-security/)
documents permanent warranty-bit changes for unsigned kernels or disabled critical
protections. This procedure excludes those operations. This review cannot promise
a legal warranty outcome, certify the phone's current state before connection, or
guarantee zero hardware risk. [Samsung India warranty terms](https://www.samsung.com/in/support/warranty/)
remain the manufacturer's terms. [Android ADB documentation](https://developer.android.com/tools/adb)
describes standard app deployment, debugging and uninstall behavior.

Connection alone, one smoke check or one successful patch is not a prize-level
finding. Freeze assignments and matched conditions, preserve all failures/unknowns,
measure genuine episodes and independently grade changes. A mobile performance or
utility claim requires demonstrated comparative benefit; results must determine
the claim. Do not claim a fully native testing stack: generation is native and
grading remains on the host. The paper stays a draft until that evidence is assessed.
