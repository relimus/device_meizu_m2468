#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from m2468 device
$(call inherit-product, device/meizu/m2468/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_DEVICE := m2468
PRODUCT_NAME := lineage_m2468
PRODUCT_BRAND := meizu
PRODUCT_MODEL := MEIZU 21 Note
PRODUCT_MANUFACTURER := meizu

PRODUCT_GMS_CLIENTID_BASE := android-meizu

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="Meizu_21Note_CN-user 14 UKQ1.230917.001 1716194826 release-keys" \
    BuildFingerprint=meizu/Meizu_21Note_CN/Meizu21Note:14/UKQ1.230917.001/1716194826:user/release-keys
