# py-ipfs

![IPFS Logo](ipfs.png)

[![](https://img.shields.io/badge/made%20by-Protocol%20Labs-blue.svg?style=flat-square)](http://ipn.io)
[![](https://img.shields.io/badge/project-IPFS-blue.svg?style=flat-square)](http://ipfs.io/)
[![](https://img.shields.io/badge/freenode-%23ipfs-blue.svg?style=flat-square)](http://webchat.freenode.net/?channels=%23ipfs)
[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Join the chat at https://gitter.im/ipfs/py-ipfs](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ipfs/py-ipfs?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> python implementation of ipfs

Python implementation of IPFS, the InterPlanetary File System. Not even
remotely done yet - check out [# fs1](https://github.com/ipfs/py-ipfs/issues/1) to join the project.

## Table of Contents

- [Background](#background)
  - [Organization](#organization)
- [Install](#install)
- [Usage](#usage)
- [Documentation](#documentation)
- [Roadmap](#roadmap)
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

## Install

> **Not ready for prime time yet**

## Usage

> **Also not ready for prime time yet**

## Documentation

To build the Sphinx docs, execute:
```shell
$ make -C docs/ <your favorite docs format> # html, pdf etc.
```

## Roadmap

Note: this has been lifted wholesale from [js-ipfs](https://github.com/ipfs/js-ipfs) and only lightly edited. As such, it may still contain inconsistencies until further editing.

TODO:

- Create stubs and checklist items for relevant Python modules.
- Create and link discussion issues at least for each top level.
- Remove JS discussion issues when no longer needed.

This is the roadmap according to the JS implementation. It has `Peer Routing` inside the `Network` hierarchy. The above organization has both at the same level. It also has the `Distributed Record Store` inside `Network`, while our organization diagram also has it at first level. TODO: harmonise?

- Block
- MerkleDAG
    - [ ] MerkleDAG Python implementation (needs IPLD).
        - [ ] [py-merkledag-store] No spec yet.
        - [Go Impl](https://github.com/ipfs/go-ipfs/blob/master/merkledag/merkledag.go)
        - [JS Impl](https://github.com/diasdavid/js-merkledag-store).
- Network
    - [ ] The `libp2p-website` [is the spec](https://github.com/diasdavid/libp2p-website), but for now the place to go is the [roadmap readme](https://github.com/diasdavid/go-libp2p/blob/docs/roadmap/README.md) in the `go-libp2p` docs.
    - [ ] [py-libp2p](https://github.com/ipfs/py-ipfs/py-libp2p) _(the entry point)_.
        - Peer Routing
            - [ ] mDNS-routing
            - [ ] py-libp2p-kad-routing [JS Impl](https://github.com/diasdavid/js-libp2p-kad-routing). [JS discussion issue](https://github.com/ipfs/js-ipfs/issues/18).
        - Discovery: listed separately because they have separate discussion issues in the JS repo, which might be relevant.
            - [ ] py-libp2p-mdns-discovery [JS Impl](https://github.com/diasdavid/js-libp2p-mdns-discovery) _mDNS-discovery_. [JS discussion issue](https://github.com/ipfs/js-ipfs/issues/19).
            - [ ] py-libp2p-random-walk [JS Impl](https://github.com/diasdavid/js-libp2p-random-walk). [JS discussion issue](https://github.com/ipfs/js-ipfs/issues/20).
            - [ ] py-libp2p-railing [JS Impl](https://github.com/diasdavid/js-libp2p-railing) _Bootstrap-list_. [JS discussion issue](https://github.com/ipfs/js-ipfs/issues/21).
        - [ ] Swarm.
            - Entry point, for now let's call it py-libp2p-swarm. [JS Impl](https://github.com/diasdavid/js-libp2p-swarm). [JS discussion issue](https://github.com/ipfs/js-ipfs/issues/22).
            - [ ] libp2p-identify [JS implementation](https://github.com/diasdavid/js-libp2p-swarm/tree/master/src/identify).
            - [ ] libp2p-ping [JS Impl](https://github.com/diasdavid/js-ipfs-ping).
            - Transports: Links to JS impementations probably not needed if we go with Curio, but there's always time to delete.
                - [ ] libp2p-tcp [JS Impl](https://github.com/diasdavid/js-libp2p-tcp)
                - [ ] libp2p-udp [JS Impl](https://github.com/diasdavid/js-libp2p-udp)
                - [ ] libp2p-udt [JS Impl](https://github.com/diasdavid/js-libp2p-udt)
                - [ ] libp2p-utp [JS Impl](https://github.com/diasdavid/js-libp2p-utp)
                - [ ] libp2p-webrtc
                - [ ] libp2p-cjdns
            - Upgrades/Crypto channel
                - [ ] libp2p-tls
                - [ ] libp2p-secio
            - Stream Muxing
                - [ ] py-spdy-stream-muxer [JS Impl](https://github.com/diasdavid/js-spdy-stream-muxer) _stream muxer_. [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/23).
                - [ ] libp2p-spdy [JS Impl](https://github.com/diasdavid/js-libp2p-spdy/blob/master/src/index.js) _stream muxer upgrade_
        - [ ] Distributed Record Store. [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/25).
            - [ ] py-libp2p-record [JS Impl](https://github.com/diasdavid/js-libp2p-record) _record (needs MerkleDAG node)_.
            - [ ] py-libp2p-distributed-record-store [JS Impl](https://github.com/diasdavid/js-libp2p-distributed-record-store).
            - [ ] py-libp2p-kad-record-store [JS Impl](https://github.com/diasdavid/js-libp2p-kad-record-store) _implements abstract record store_.
- Exchange
    - [ ] py-bitswap [JS Impl](https://github.com/diasdavid/js-bitswap). [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/17).
- Supporting modules
    - multihash/multihashing: (see discussion about the [multihash/multihashing distinction](https://github.com/ipfs/py-ipfs/issues/23#issuecomment-158345821))
        - [ ] [py-multihashing](https://github.com/JulienPalard/multihash) (note: started as multihash, should be multihashing) [JS Impl](https://github.com/jbenet/js-multihashing)
        - [ ] [py-multihash] [Spec](https://github.com/jbenet/multihash). [Discussion Issue](https://github.com/ipfs/py-ipfs/issues/13). [Go Impl](https://github.com/jbenet/go-multihash). [JS Impl](https://github.com/jbenet/js-multihash)
    - [ ] [python-multiaddr](https://github.com/amstocker/python-multiaddr) [Spec](https://github.com/jbenet/multiaddr) [Go Impl](https://github.com/jbenet/go-multiaddr). [JS Impl](https://github.com/jbenet/js-multiaddr).
    - [ ] py-multistream [Spec](https://github.com/jbenet/multistream). [JS Impl](https://github.com/diasdavid/js-multistream) _protocol muxer_. [JS Discussion issue](https://github.com/ipfs/js-ipfs/issues/24).
    - [ ] [py-multicodec](https://github.com/fredthomsen/py-multicodec). [Spec](https://github.com/jbenet/multicodec). [Go Impl](https://github.com/jbenet/go-multicodec)
    - [ ] PeerID - [JS Impl](https://github.com/diasdavid/js-peer-id)
    - [ ] PeerInfo - [JS Impl](https://github.com/diasdavid/js-peer-info)
    - [ ] repo
    - [ ] [py-ipld](https://github.com/bigchaindb/py-ipld). [Spec](https://github.com/ipfs/specs/pull/37). [Discussion](https://github.com/ipfs/go-ipld/issues/8). [Go Impl.](https://github.com/ipfs/go-ipld). [JS Impl.](https://github.com/diasdavid/js-ipld)
- [specs/19](https://github.com/ipfs/specs/pull/19).


## Contribute

IPFS implementation in Python is a work in progress. As such, there's a few things you can do right now to help out:

  * Go through the modules above and **check out existing issues**. This would be especially useful for modules in active development. Some knowledge of IPFS may be required, as well as the infrasture behind it - for instance, you may need to read up on p2p and more complex operations like muxing to be able to help technically. However, don't let this discourage you! Feel free to ask questions about where to get that knowledge in this repo, or jump into IRC and ask questions there. We're here to help.
  * **Perform code reviews**. More eyes will help a) speed the project along b) ensure quality and c) reduce possible future bugs.
  * Take a look at both [go-ipfs](https://github.com/ipfs/go-ipfs) and [js-ipfs](https://github.com/ipfs/js-ipfs) (which we intend to follow to a point), and also at some of the planning repositories or issues: for instance, the libp2p spec [here](https://github.com/libp2p/specs). Contributions here that would be most helpful are **top-level comments** about how it should look based on our understanding. Again, the more eyes the better.
  * **Add tests**. There can never be enough tests.
  * **Contribute to the [FAQ repository](https://github.com/ipfs/faq/issues)** with any questions you have about IPFS or any of the relevant technology. A good example would be asking, "What is a merkledag tree?". If you don't know a term, odds are someone else doesn't either. Eventually, we should have a good understanding of where we need to improve communications and teaching together to make IPFS and IPN better.
  * TODO: write our own `CONTRIBUTE.md` similar to [IPFS's](https://github.com/ipfs/ipfs/blob/master/CONTRIBUTE.md) and once we know what we're doing and who's doing it.

Please be aware that all interactions related to multiformats are subject to the IPFS [Code of Conduct](https://github.com/ipfs/community/blob/master/code-of-conduct.md).

## License

[MIT](LICENSE)
