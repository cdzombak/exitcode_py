from typing import Final


# SUCCESS: Generic success code. (from libc)
SUCCESS: Final = 0

# FAILURE: Generic failure or unspecified error. (from libc)
FAILURE: Final = 1

# INVALIDARGUMENT: Invalid or excess arguments. (from LSB)
INVALIDARGUMENT: Final = 2

# NOTIMPLEMENTED: Unimplemented feature. (from LSB)
NOTIMPLEMENTED: Final = 3

# NOPERMISSION: The user has insufficient privileges. (from LSB)
NOPERMISSION: Final = 4

# NOTINSTALLED: The program is not installed. (from LSB)
NOTINSTALLED: Final = 5

# NOTCONFIGURED: The program is not configured. (from LSB)
NOTCONFIGURED: Final = 6

# NOTRUNNING: The program is not running. (from LSB)
NOTRUNNING: Final = 7

# USAGE: Command line usage error (from BSD)
USAGE: Final = 64

# DATAERR: Data format error (from BSD)
DATAERR: Final = 65

# NOINPUT: Cannot open input (from BSD)
NOINPUT: Final = 66

# NOUSER: Addressee unknown (from BSD)
NOUSER: Final = 67

# NOHOST: Host name unknown (from BSD)
NOHOST: Final = 68

# UNAVAILABLE: Service unavailable (from BSD)
UNAVAILABLE: Final = 69

# SOFTWARE: internal software error (from BSD)
SOFTWARE: Final = 70

# OSERR: System error (e.g., can't fork) (from BSD)
OSERR: Final = 71

# OSFILE: Critical OS file missing (from BSD)
OSFILE: Final = 72

# CANTCREAT: Can't create (user) output file (from BSD)
CANTCREAT: Final = 73

# IOERR: Input/output error (from BSD)
IOERR: Final = 74

# TEMPFAIL: Temporary failure; user is invited to retry (from BSD)
TEMPFAIL: Final = 75

# PROTOCOL: Remote error in protocol (from BSD)
PROTOCOL: Final = 76

# NOPERM_BSD: Permission denied (from BSD)
NOPERM_BSD: Final = 77

# CONFIG_BSD: Configuration error (from BSD)
CONFIG_BSD: Final = 78

# CHDIR: Changing to the requested working directory failed. (from systemd)
CHDIR: Final = 200

# NICE: Failed to set up process scheduling priority (nice level). (from systemd)
NICE: Final = 201

# FDS: Failed to close unwanted file descriptors, or to adjust passed file descriptors. (from systemd)
FDS: Final = 202

# EXEC: The actual process execution failed (specifically, the execve(2) system call). Most likely this is caused by a missing or non-accessible executable file. (from systemd)
EXEC: Final = 203

# MEMORY: Failed to perform an action due to memory shortage. (from systemd)
MEMORY: Final = 204

# LIMITS: Failed to adjust resource limits. (from systemd)
LIMITS: Final = 205

# OOM_ADJUST: Failed to adjust the OOM setting. (from systemd)
OOM_ADJUST: Final = 206

# SIGNAL_MASK: Failed to set process signal mask. (from systemd)
SIGNAL_MASK: Final = 207

# STDIN: Failed to set up standard input. (from systemd)
STDIN: Final = 208

# STDOUT: Failed to set up standard output. (from systemd)
STDOUT: Final = 209

# CHROOT: Failed to change root directory (chroot(2)). (from systemd)
CHROOT: Final = 210

# IOPRIO: Failed to set up IO scheduling priority. (from systemd)
IOPRIO: Final = 211

# TIMERSLACK: Failed to set up timer slack. (from systemd)
TIMERSLACK: Final = 212

# SECUREBITS: Failed to set process secure bits. (from systemd)
SECUREBITS: Final = 213

# SETSCHEDULER: Failed to set up CPU scheduling. (from systemd)
SETSCHEDULER: Final = 214

# CPUAFFINITY: Failed to set up CPU affinity. (from systemd)
CPUAFFINITY: Final = 215

# GROUP: Failed to determine or change group credentials. (from systemd)
GROUP: Final = 216

# USER: Failed to determine or change user credentials, or to set up user namespacing. (from systemd)
USER: Final = 217

# CAPABILITIES: Failed to drop capabilities, or apply ambient capabilities. (from systemd)
CAPABILITIES: Final = 218

# CGROUP: Setting up the service control group failed. (from systemd)
CGROUP: Final = 219

# SETSID: Failed to create new process session. (from systemd)
SETSID: Final = 220

# CONFIRM: Execution has been cancelled by the user. See the systemd.confirm_spawn= kernel command line setting on kernel-command-line(7) for details. (from systemd)
CONFIRM: Final = 221

# STDERR: Failed to set up standard error output. (from systemd)
STDERR: Final = 222

# PAM: Failed to set up PAM session. (from systemd)
PAM: Final = 224

# NETWORK: Failed to set up network namespacing. (from systemd)
NETWORK: Final = 225

# NAMESPACE: Failed to set up mount, UTS, or IPC namespacing. (from systemd)
NAMESPACE: Final = 226

# NO_NEW_PRIVILEGES: Failed to disable new privileges. (from systemd)
NO_NEW_PRIVILEGES: Final = 227

# SECCOMP: Failed to apply system call filters. (from systemd)
SECCOMP: Final = 228

# SELINUX_CONTEXT: Determining or changing SELinux context failed. (from systemd)
SELINUX_CONTEXT: Final = 229

# PERSONALITY: Failed to set up an execution domain (personality). (from systemd)
PERSONALITY: Final = 230

# APPARMOR_PROFILE: Failed to prepare changing AppArmor profile. (from systemd)
APPARMOR_PROFILE: Final = 231

# ADDRESS_FAMILIES: Failed to restrict address families. (from systemd)
ADDRESS_FAMILIES: Final = 232

# RUNTIME_DIRECTORY: Setting up runtime directory failed. (from systemd)
RUNTIME_DIRECTORY: Final = 233

# CHOWN: Failed to adjust socket ownership. Used for socket units only. (from systemd)
CHOWN: Final = 235

# SMACK_PROCESS_LABEL: Failed to set SMACK label. (from systemd)
SMACK_PROCESS_LABEL: Final = 236

# KEYRING: Failed to set up kernel keyring. (from systemd)
KEYRING: Final = 237

# STATE_DIRECTORY: Failed to set up unit's state directory. (from systemd)
STATE_DIRECTORY: Final = 238

# CACHE_DIRECTORY: Failed to set up unit's cache directory. (from systemd)
CACHE_DIRECTORY: Final = 239

# LOGS_DIRECTORY: Failed to set up unit's logging directory. (from systemd)
LOGS_DIRECTORY: Final = 240

# CONFIGURATION_DIRECTORY: Failed to set up unit's configuration directory. (from systemd)
CONFIGURATION_DIRECTORY: Final = 241

# NUMA_POLICY: Failed to set up unit's NUMA memory policy. (from systemd)
NUMA_POLICY: Final = 242

# CREDENTIALS: Failed to set up unit's credentials. (from systemd)
CREDENTIALS: Final = 243

# BPF: Failed to apply BPF restrictions. (from systemd)
BPF: Final = 245

