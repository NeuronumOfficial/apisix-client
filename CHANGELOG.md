# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2026-06-11

### Added

- Added support for `proxy-rewrite` plugin.

## [0.6.0] - 2026-05-20

### Added

- Added support for `basic-auth` plugin.
- Added support for `file-logger` plugin.
- Added support for `consumer-restriction` plugin.

### Changed

- Restructured plugins module. Separated to submodules based on plugin categories in APISIX documentation.


## [0.5.0] - 2025-10-04

### Added

- Added support for service management.
- Added support for `clickhouse-logger` plugin.


## [0.4.0] - 2025-10-04

### Added

- Added support for upstream management.


## [0.3.0] - 2025-10-04

### Added

- Added factory to generate response classes.

### Changed

- Exactly defined Response classes were replaced with generated classes.


## [0.2.0] - 2025-09-27

### Added

- APISIX python client for admin API.
  - Added support for consumer management.
  - Added support for route management.
  - Added support for plugin management.
    - Added support for `key-auth` plugin.
    - Added support for `limits-count` plugin.

