# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2026-07-31

## Changed
- Remove unnecessary debug logging.

## [1.0.2] - 2026-07-31

## Changed
- Added support for `jsonschema` validation of plugin properties.

## [1.0.1] - 2026-07-31

## Changed
- Moved `converter` to `apisix_client.converter.py` file. It was previously in `apisix_client.base_models.py` file. It lead to circular import issues when using `converter` in plugins module. Now it is possible to use `converter` in plugins module without any issues.

## [1.0.0] - 2026-07-30

## Changed
- Changed the way plugins are handled in the client. Possibility to use whatever plugin even is not defined in this library. Minimum. requirement is attrs class implementing Plugin Protocol.

## [0.9.0] - 2026-06-18
 - Added support for `request-validation` plugin.

## [0.8.2] - 2026-06-15

## Changed
- Remove obsolete imports in plugins module.

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

