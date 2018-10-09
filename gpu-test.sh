#!/bin/bash
echo "Listing devices:"
ls /dev/nv*
echo "GPU info:"
nvidia-smi --query
echo "Listing GPUs:"
nvidia-smi --list-gpus