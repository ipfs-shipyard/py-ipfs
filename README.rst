.. image::  ipfs.png

#######
py-ipfs
#######

Python implementation of IPFS, the InterPlanetary File System. Not even
remotely done yet - check out `#1`__ to join the project.

.. __: https://github.com/ipfs/py-ipfs/issues/1

IPFS is a distributed file system that seeks to connect all computing devices
with the same system of files. In some ways, this is similar to the original
aims of the Web, but IPFS is actually more similar to a single bittorrent swarm
exchanging git objects.

IPFS could become a new major subsystem of the internet. If built right, it
could complement or replace HTTP. It could complement or replace even more. It
sounds crazy. It *is* crazy.

Take a look at the main repo_.

############
Organization
############

This repository contains the Python package `ipfs`, which contains the
subpackages `block`, `merkledag`, `naming`, and `routing`, which function as
laid out in the main IPFS repo_.

.. _repo: http://github.com/ipfs/ipfs

The repo roughly looks like this:

```
ipfs
├─ block
├─ merkledag
├─ naming
├─ network
└─ routing
```
