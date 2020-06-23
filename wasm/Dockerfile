FROM rust
RUN curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
RUN mkdir /code
WORKDIR /code
RUN cargo install cargo-generate
RUN cargo install cargo-web
