#!/usr/bin/env python
import os

words = ["Hello","world", "from"]
words.append(os.environ["SLURMD_NODENAME"])
words.append("with")
words.append(os.environ["SLURM_CPUS_ON_NODE"])
words.append("CPUs")

out_string = " ".join(words)
print(out_string)
