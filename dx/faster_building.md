# Faster builds in Rust

1. Use faster linker

- https://github.com/davidlattimore/wild
- https://github.com/rui314/mold

2. Use `cargo wizard`

```
cargo wizard apply fast-compile dev

cargo wizard apply fast-runtime release
```

Install `lld` on macOS:

```
brew install llvm

brew install lld
```
