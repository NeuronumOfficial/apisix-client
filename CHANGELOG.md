# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.1] - 2026-06-15

### Added
- Fix `response-rewrite` plugin properties in Plugins class.

## [0.8.0] - 2026-06-15

### Added
- Added support for `response-rewrite` plugin.

## [0.7.2] - 2026-06-11

### Changed
- Fix basic-auth plugin properties in Plugins class.
- Fix proxy-rewrite 

## [0.7.1] - 2026-06-11

### Changed
- Fix non-required properties of `limit-count` plugin.
- Added missing `limit-count` plugin properties.

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

