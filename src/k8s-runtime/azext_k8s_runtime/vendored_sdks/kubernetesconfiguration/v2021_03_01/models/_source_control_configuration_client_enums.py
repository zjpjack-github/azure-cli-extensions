# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ComplianceStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The compliance state of the configuration."""

    PENDING = "Pending"
    COMPLIANT = "Compliant"
    NONCOMPLIANT = "Noncompliant"
    INSTALLED = "Installed"
    FAILED = "Failed"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Enum0(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum0."""

    MICROSOFT_CONTAINER_SERVICE = "Microsoft.ContainerService"
    MICROSOFT_KUBERNETES = "Microsoft.Kubernetes"


class Enum1(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum1."""

    MANAGED_CLUSTERS = "managedClusters"
    CONNECTED_CLUSTERS = "connectedClusters"


class MessageLevelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level of the message."""

    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"


class OperatorScopeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scope at which the operator will be installed."""

    CLUSTER = "cluster"
    NAMESPACE = "namespace"


class OperatorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the operator."""

    FLUX = "Flux"


class ProvisioningStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the resource provider."""

    ACCEPTED = "Accepted"
    DELETING = "Deleting"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
