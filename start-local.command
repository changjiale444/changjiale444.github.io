#!/bin/zsh
set -e
cd "$(dirname "$0")"
if command -v node >/dev/null 2>&1; then
  JIALE_NODE="$(command -v node)"
else
  JIALE_NODE="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
fi
if [[ ! -x "$JIALE_NODE" ]]; then
  echo 'Please install Node.js 24 or later, then run this script again.'
  exit 1
fi
export PATH="$(dirname "$JIALE_NODE"):$PATH"
export ASTRO_TELEMETRY_DISABLED=1
if [[ ! -d node_modules ]]; then
  "$JIALE_NODE" .yarn/releases/yarn-4.13.0.cjs install --immutable
fi
exec "$JIALE_NODE" .yarn/releases/yarn-4.13.0.cjs dev --host 127.0.0.1
