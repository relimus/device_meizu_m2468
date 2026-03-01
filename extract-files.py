#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups_user_type,
)

blob_fixups: blob_fixups_user_type = {
    (
    'system_ext/lib/libmiracastsystem.so',
    'system_ext/lib64/libmiracastsystem.so',
    ): blob_fixup()
        .remove_needed('libmdnssd.so')
        .replace_needed('android.media.audio.common.types-V2-cpp', 'android.media.audio.common.types-V4-cpp'),
    'vendor/lib64/libwfdhdcpservice_proprietary.so': blob_fixup()
        .remove_needed('libclang_rt.ubsan_standalone-aarch64-android.so'),
    'vendor/bin/hw/android.hardware.power-service': blob_fixup()
        .replace_needed('android.hardware.power-V3-ndk', 'android.hardware.power-V4-ndk'),
    'vendor/bin/hw/android.hardware.health-service.qti': blob_fixup()
        .replace_needed('android.hardware.health-V1-ndk', 'android.hardware.health-V4-ndk'),
    (
    'vendor/lib/hw/android.hardware.bluetooth.audio-impl-qti.so',
    'vendor/lib64/hw/android.hardware.bluetooth.audio-impl-qti.so',
    ): blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V2-ndk', 'android.hardware.bluetooth.audio-V5-ndk')
        .replace_needed('android.hardware.audio.common-V1-ndk', 'android.hardware.audio.common-V4-ndk'),

    'vendor/bin/hw/wpa_supplicant': blob_fixup()
        .replace_needed('android.hardware.wifi.supplicant-V1-ndk', 'android.hardware.wifi.supplicant-V4-ndk'),
    'vendor/bin/hw/android.hardware.sensors-service.multihal': blob_fixup()
        .replace_needed('android.hardware.sensors-V1-ndk', 'android.hardware.sensors-V3-ndk'),
    (
    'vendor/lib/btaudio_offload_if.so',
    'vendor/lib/hw/audio.bluetooth.default.so',
    'vendor/lib/hw/audio.bluetooth_qti.default.so',
    'vendor/lib/libbluetooth_audio_session_aidl.so',
    'vendor/lib/libbluetooth_audio_session_aidl_qti.so',
    'vendor/lib64/btaudio_offload_if.so',
    'vendor/lib64/hw/audio.bluetooth.default.so',
    'vendor/lib64/hw/audio.bluetooth_qti.default.so',
    'vendor/lib64/libbluetooth_audio_session_aidl.so',
    'vendor/lib64/libbluetooth_audio_session_aidl_qti.so',
    ): blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V2-ndk', 'android.hardware.bluetooth.audio-V5-ndk'),
    (
    'system_ext/lib/libwfdservice.so',
    'system_ext/lib64/libwfdservice.so',
    ): blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp', 'android.media.audio.common.types-V4-cpp'),
}

lib_fixups: lib_fixups_user_type = {

    'libmdnssd': lib_fixup_remove,
}

namespace_imports = [
    'device/meizu/m2468',
    'hardware/qcom-caf/sm8550',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]

module = ExtractUtilsModule(
    'm2468',
    'meizu',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
