# py-ipfs

![IPFS Logo](ipfs.png)

[![Made by the IPFS Community](https://img.shields.io/badge/made%20by-IPFS%20Community-blue.svg?style=flat-square)](https://docs.ipfs.io/community/)
[![](https://img.shields.io/badge/project-IPFS-blue.svg?style=flat-square)](http://ipfs.io/)
[![IRC #py-ipfs on chat.freenode.net](https://img.shields.io/badge/freenode%20IRC-%23py--ipfs-blue.svg?style=flat-square)](http://webchat.freenode.net/?channels=%23py-ipfs)
[![Matrix #py-ipfs:ninetailed.ninja](https://img.shields.io/matrix/py-ipfs:ninetailed.ninja?color=blue&label=matrix+chat&style=flat-square)](https://matrix.to/#/#py-ipfs:ninetailed.ninja?via=ninetailed.ninja&via=librem.one)
[![Standard README Compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Python implementation of IPFS

Python implementation of IPFS, the InterPlanetary File System. **Not even
remotely done yet.**

For the current status, and where you can help, please see [issue 49](https://github.com/ipfs/py-ipfs/issues/49).

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contribute](#contribute)
- [License](#license)

## Background

IPFS is a distributed file system that seeks to connect all computing devices
with the same system of files. In some ways, this is similar to the original
aims of the Web, but IPFS is actually more similar to a single bittorrent swarm
exchanging git objects.

IPFS could become a new major subsystem of the internet. If built right, it
could complement or replace HTTP. It could complement or replace even more. It
sounds crazy. It *is* crazy.

<!--
### Organization

This repository contains the Python package `ipfs`, which contains the
subpackages `block`, `merkledag`, `naming`, and `routing`, which function as
laid out in [the main IPFS repo](http://github.com/ipfs/ipfs)

The repo roughly looks like this::

    ipfs
    ├─ block
    ├─ merkledag
    ├─ naming
    ├─ network
    └─ routing
-->

## Install

> **Not ready for prime time yet**

## Usage

> **Also not ready for prime time yet**

## Documentation

To build the Sphinx docs, execute:
```shell
$ make -C docs/ <your favorite docs format> # html, pdf etc.
```

<!--
## Roadmap

Note: This is based on the roadmap from [js-ipfs](https://github.com/ipfs/js-ipfs) . As such, it may still contain inconsistencies until further editing.

- Block
- MerkleDAG
    - [ ] MerkleDAG Python implementation (needs IPLD).
        - [ ] [py-merkledag-store] No spec yet.
        - [Go Impl](https://github.com/ipfs/go-ipfs/blob/master/merkledag/merkledag.go)
        - [JS Impl](https://github.com/diasdavid/js-merkledag-store).
- Network
    - [ ] The `libp2p-website` [is the spec](https://github.com/diasdavid/libp2p-website), but for now the place to go is the [roadmap readme](https://github.com/diasdavid/go-libp2p/blob/docs/roadmap/README.md) in the `go-libp2p` docs.
    - [ ] [py-libp2p](https://github.com/libp2p/py-libp2p)
        - Please see the [py-libp2p repository](https://github.com/libp2p/py-libp2p#feature-breakdown)
          for the most up-to-date status of different components.
        - [ ] Swarm
            - The following modules are required, as a minimum, for basic connectivity:
                - [ ] libp2p-identify [JS implementation](https://github.com/diasdavid/js-libp2p-swarm/tree/master/src/identify).
                - Transports (just the baseline requirements, every module helps)
                    - [X] TCP [JS Impl](https://github.com/diasdavid/js-libp2p-tcp)
                - Stream Multiplexer
                    - [X] mplex
                - Upgrades/Crypto channel
                    - [ ] libp2p-secio
                - Peer Discovery (just the baseline requirements, every module helps)
                    - [X] bootstrap list
                    - [ ] Kademlia DHT
                    - [ ] mDNS
                - Content Discovery (just the baseline requirements, every module helps)
                    - [ ] Kademlia DHT
                - NAT Traversal (just the baseline requirements, every module helps)
                    - [ ] UPnP
                    - [ ] NAT-PmP
- Exchange
    - [ ] py-bitswap [JS Impl](https://github.com/diasdavid/js-bitswap). [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/17).
- Supporting modules
    - [X] [py-cid](https://github.com/ipld/py-cid)
    - [X] [py-multiaddr](https://github.com/multiformats/py-multiaddr) [Spec](https://github.com/jbenet/multiaddr) [Go Impl](https://github.com/jbenet/go-multiaddr). [JS Impl](https://github.com/jbenet/js-multiaddr).
    - [ ] [py-multistream-select](https://github.com/dheatovwil/py-multistream-select) [Spec](https://github.com/jbenet/multistream). [JS Impl](https://github.com/diasdavid/js-multistream) _protocol muxer_. [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/24).
    - [X] [py-multicodec](https://github.com/multiformats/py-multicodec). [Spec](https://github.com/jbenet/multicodec). [Go Impl](https://github.com/jbenet/go-multicodec)
    - [ ] [py-ipld](https://github.com/ipld/py-ipld-dag). [Spec](https://github.com/ipfs/specs/pull/37). [Discussion](https://github.com/ipfs/go-ipld/issues/8). [Go Impl.](https://github.com/ipfs/go-ipld). [JS Impl.](https://github.com/diasdavid/js-ipld)
-->


## Contribute

IPFS implementation in Python is a work in progress. As such, there's a few things you can do right now to help out:

  * Get in touch! You can find us on [#py-ipfs on chat.freenode.org](http://webchat.freenode.net/?channels=%23py-ipfs)!
     * A [Matrix chat option](https://matrix.to/#/#py-ipfs:ninetailed.ninja?via=ninetailed.ninja&via=librem.one) is also provided. Please note however that, at the time of writing, the default `matrix.org` server is severely overloaded and your messages may only arrive with extreme delay; using a different homeserver is hence highly recommended.
  * **Check out [issue 49](https://github.com/ipfs/py-ipfs/issues/49) for an up-to-date list** (maintained by @alexander255) **of tasks** that could use your help. Feel free to ask questions on that and we'll try to help. Be sure to drop a note if there is anything you'd like to work on and we'll update the issue to let others know.
  * **Perform code reviews**. More eyes will help a) speed the project along b) ensure quality and c) reduce possible future bugs.
  * Take a look at both [go-ipfs](https://github.com/ipfs/go-ipfs) and [js-ipfs](https://github.com/ipfs/js-ipfs) (which we intend to follow to a point), and also at some of the planning repositories or issues: for instance, the libp2p spec [here](https://github.com/libp2p/specs). Contributions here that would be most helpful are **top-level comments** about how it should look based on our understanding. Again, the more eyes the better.
  * **Add tests**. There can never be enough tests.
  * **Contribute to the [FAQ repository](https://github.com/ipfs/faq/issues)** with any questions you have about IPFS or any of the relevant technology. A good example would be asking, "What is a merkledag tree?". If you don't know a term, odds are someone else doesn't either. Eventually, we should have a good understanding of where we need to improve communications and teaching together to make IPFS and IPN better.
  * TODO: write our own `CONTRIBUTE.md` similar to [IPFS's](https://github.com/ipfs/ipfs/blob/master/CONTRIBUTE.md) and once we know what we're doing and who's doing it.

Please be aware that all interactions related to IPFS, libp2p and Multiformats are subject to the IPFS [Code of Conduct](https://github.com/ipfs/community/blob/master/code-of-conduct.md).

## License

[MIT](LICENSE)
