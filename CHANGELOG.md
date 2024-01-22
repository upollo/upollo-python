# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

## [Unreleased]

### Changed

### Added

### Removed

## [0.1.1] 2024-01-22

### Added

- TRIALED_ON_OTHER_ACCOUNT flag type, which is available for customers with billing
  and subscription data connected.
- COMMERCIAL_USER, PAYMENT_NAME_DIFFERS and LIMITED_DEVICE_INFORMATION flag types.

## [0.1.0] 2022-09-26

### Changed

- rename from userwatch to upollo.
  - rename pypi package name from `userwatch-python` `upollo-python`
  - rename imports `from userwatch import userwatch` & `from userwatch import userwatch_public_pb2` to  `from upollo import upollo` & `from upollo import upollo_public_pb2`
  - rename client `userwatch.Userwatch` to `upollo.Upollo`

## [0.0.6] 2022-09-14

### Added

- Additional logging on errors

## [0.0.5] 2022-09-02

### Changed

- updated protobuf dependency

## [0.0.4] 2022-08-19

### Changed

- flags were renamed to remove the `FLAG_TYPE` prefix, eg `userwatch_public_pb2.FLAG_TYPE_MULTIPLE_ACCOUNTS` becomes `userwatch_public_pb2.MULTIPLE_ACCOUNTS`
- `validate` was renamed to `verify` and the `event_type` argument was removed.
  - `userwatch_client.validate(userwatch_token, user_info, event_type)` becomes
  - `userwatch_client.verify(userwatch_token, user_info)`

### Removed

- the flag type `userwatch_public_pb2.FLAG_TYPE_REPEATED_ACTION` has been removed.

### Added

- A retry was added to prevent intermittent network errors.
