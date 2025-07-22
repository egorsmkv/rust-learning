Run:

```
cd which-linker

cargo build -vvvv
```

Output:

```
Compiling which-linker v0.1.0 (/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker)
     Running `CARGO=/Users/yehorsmoliakov/.rustup/toolchains/stable-aarch64-apple-darwin/bin/cargo CARGO_BIN_NAME=which-linker CARGO_CRATE_NAME=which_linker CARGO_MANIFEST_DIR=/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker CARGO_MANIFEST_PATH=/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker/Cargo.toml CARGO_PKG_AUTHORS='' CARGO_PKG_DESCRIPTION='' CARGO_PKG_HOMEPAGE='' CARGO_PKG_LICENSE='' CARGO_PKG_LICENSE_FILE='' CARGO_PKG_NAME=which-linker CARGO_PKG_README='' CARGO_PKG_REPOSITORY='' CARGO_PKG_RUST_VERSION='' CARGO_PKG_VERSION=0.1.0 CARGO_PKG_VERSION_MAJOR=0 CARGO_PKG_VERSION_MINOR=1 CARGO_PKG_VERSION_PATCH=0 CARGO_PKG_VERSION_PRE='' CARGO_PRIMARY_PACKAGE=1 CARGO_SBOM_PATH='' DYLD_FALLBACK_LIBRARY_PATH='/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker/target/debug/deps:/Users/yehorsmoliakov/.rustup/toolchains/stable-aarch64-apple-darwin/lib:/Users/yehorsmoliakov/lib:/usr/local/lib:/usr/lib' /Users/yehorsmoliakov/.rustup/toolchains/stable-aarch64-apple-darwin/bin/rustc --crate-name which_linker --edition=2024 src/main.rs --error-format=json --json=diagnostic-rendered-ansi,artifacts,future-incompat --diagnostic-width=251 --crate-type bin --emit=dep-info,link -C embed-bitcode=no -C debuginfo=2 -C split-debuginfo=unpacked --check-cfg 'cfg(docsrs,test)' --check-cfg 'cfg(feature, values())' -C metadata=dd797266c6d2f9fe -C extra-filename=-1c0655113c6c4432 --out-dir /Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker/target/debug/deps -C incremental=/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker/target/debug/incremental -L dependency=/Users/yehorsmoliakov/Downloads/rust-learning/research/which-linker-used/which-linker/target/debug/deps`
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.16s
```

---

Check:

Specify own linker:

```
RUSTFLAGS="-C linker=rust-lld" cargo build -vvv
```

---

On Linux:

```
sudo apt install mold
```

```
cargo build -vvv
```

Output:

```
Compiling which-linker v0.1.0 (/home/yehor/Work/rust-learning/research/which-linker-used/which-linker)
     Running `CARGO=/home/yehor/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/cargo CARGO_BIN_NAME=which-linker CARGO_CRATE_NAME=which_linker CARGO_MANIFEST_DIR=/home/yehor/Work/rust-learning/research/which-linker-used/which-linker CARGO_MANIFEST_PATH=/home/yehor/Work/rust-learning/research/which-linker-used/which-linker/Cargo.toml CARGO_PKG_AUTHORS='' CARGO_PKG_DESCRIPTION='' CARGO_PKG_HOMEPAGE='' CARGO_PKG_LICENSE='' CARGO_PKG_LICENSE_FILE='' CARGO_PKG_NAME=which-linker CARGO_PKG_README='' CARGO_PKG_REPOSITORY='' CARGO_PKG_RUST_VERSION='' CARGO_PKG_VERSION=0.1.0 CARGO_PKG_VERSION_MAJOR=0 CARGO_PKG_VERSION_MINOR=1 CARGO_PKG_VERSION_PATCH=0 CARGO_PKG_VERSION_PRE='' CARGO_PRIMARY_PACKAGE=1 CARGO_SBOM_PATH='' LD_LIBRARY_PATH='/home/yehor/Work/rust-learning/research/which-linker-used/which-linker/target/debug/deps:/home/yehor/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib' /home/yehor/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc --crate-name which_linker --edition=2024 src/main.rs --error-format=json --json=diagnostic-rendered-ansi,artifacts,future-incompat --diagnostic-width=245 --crate-type bin --emit=dep-info,link -C embed-bitcode=no -C debuginfo=2 --check-cfg 'cfg(docsrs,test)' --check-cfg 'cfg(feature, values())' -C metadata=cf49da4677904325 -C extra-filename=-104b27002703aec2 --out-dir /home/yehor/Work/rust-learning/research/which-linker-used/which-linker/target/debug/deps -C linker=clang -C incremental=/home/yehor/Work/rust-learning/research/which-linker-used/which-linker/target/debug/incremental -L dependency=/home/yehor/Work/rust-learning/research/which-linker-used/which-linker/target/debug/deps -C link-arg=-fuse-ld=/usr/bin/mold`
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.19s
```
