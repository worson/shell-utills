echo "scp from $SSH_ADR:$2 to $1"
scp "$SSH_ADR:$1" "$2"
