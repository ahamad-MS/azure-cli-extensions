# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class CreatedBy(Model):
    """Provides details of the entity that created/updated the workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar oid: The Object ID that created the workspace.
    :vartype oid: str
    :ivar puid: The Personal Object ID corresponding to the object ID above
    :vartype puid: str
    :ivar application_id: The application ID of the application that initiated
     the creation of the workspace. For example, Azure Portal.
    :vartype application_id: str
    """

    _validation = {
        'oid': {'readonly': True},
        'puid': {'readonly': True},
        'application_id': {'readonly': True},
    }

    _attribute_map = {
        'oid': {'key': 'oid', 'type': 'str'},
        'puid': {'key': 'puid', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CreatedBy, self).__init__(**kwargs)
        self.oid = None
        self.puid = None
        self.application_id = None


class Encryption(Model):
    """The object that contains details of encryption used on the workspace.

    :param key_source: The encryption keySource (provider). Possible values
     (case-insensitive):  Default, Microsoft.Keyvault. Possible values include:
     'Default', 'Microsoft.Keyvault'. Default value: "Default" .
    :type key_source: str or ~azure.mgmt.databricks.models.KeySource
    :param key_name: The name of KeyVault key.
    :type key_name: str
    :param key_version: The version of KeyVault key.
    :type key_version: str
    :param key_vault_uri: The Uri of KeyVault.
    :type key_vault_uri: str
    """

    _attribute_map = {
        'key_source': {'key': 'keySource', 'type': 'str'},
        'key_name': {'key': 'KeyName', 'type': 'str'},
        'key_version': {'key': 'keyversion', 'type': 'str'},
        'key_vault_uri': {'key': 'keyvaulturi', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Encryption, self).__init__(**kwargs)
        self.key_source = kwargs.get('key_source', "Default")
        self.key_name = kwargs.get('key_name', None)
        self.key_version = kwargs.get('key_version', None)
        self.key_vault_uri = kwargs.get('key_vault_uri', None)


class ErrorDetail(Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error's code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param target: Indicates which property in the request is responsible for
     the error.
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)


class ErrorInfo(Model):
    """The code and message for an error.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. A machine readable error code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: error details.
    :type details: list[~azure.mgmt.databricks.models.ErrorDetail]
    :param innererror: Inner error details if they exist.
    :type innererror: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorInfo, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)


class ErrorResponse(Model):
    """Error response.

    Contains details when the response code indicates an error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The error details.
    :type error: ~azure.mgmt.databricks.models.ErrorInfo
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorInfo'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ManagedIdentityConfiguration(Model):
    """The Managed Identity details for storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The objectId of the Managed Identity that is linked to
     the Managed Storage account.
    :vartype principal_id: str
    :ivar tenant_id: The tenant Id where the Managed Identity is created.
    :vartype tenant_id: str
    :ivar type: The type of Identity created. It can be either SystemAssigned
     or UserAssigned.
    :vartype type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManagedIdentityConfiguration, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = None


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.databricks.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.ResourceProvider
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)


class Resource(Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Sku(Model):
    """SKU for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name.
    :type name: str
    :param tier: The SKU tier.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)


class Workspace(TrackedResource):
    """Information about workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param parameters: The workspace's custom parameters.
    :type parameters: ~azure.mgmt.databricks.models.WorkspaceCustomParameters
    :ivar provisioning_state: The workspace provisioning state. Possible
     values include: 'Accepted', 'Running', 'Ready', 'Creating', 'Created',
     'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.databricks.models.ProvisioningState
    :param ui_definition_uri: The blob URI where the UI definition file is
     located.
    :type ui_definition_uri: str
    :param authorizations: The workspace provider authorizations.
    :type authorizations:
     list[~azure.mgmt.databricks.models.WorkspaceProviderAuthorization]
    :param created_by: Indicates the Object ID, PUID and Application ID of
     entity that created the workspace.
    :type created_by: ~azure.mgmt.databricks.models.CreatedBy
    :param updated_by: Indicates the Object ID, PUID and Application ID of
     entity that last updated the workspace.
    :type updated_by: ~azure.mgmt.databricks.models.CreatedBy
    :param created_date_time: Specifies the date and time when the workspace
     is created.
    :type created_date_time: datetime
    :ivar workspace_id: The unique identifier of the databricks workspace in
     databricks control plane.
    :vartype workspace_id: str
    :ivar workspace_url: The workspace URL which is of the format
     'adb-{workspaceId}.{random}.azuredatabricks.net'
    :vartype workspace_url: str
    :param storage_account_identity: The details of Managed Identity of
     Storage Account
    :type storage_account_identity:
     ~azure.mgmt.databricks.models.ManagedIdentityConfiguration
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.databricks.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_resource_group_id': {'required': True},
        'provisioning_state': {'readonly': True},
        'workspace_id': {'readonly': True},
        'workspace_url': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'WorkspaceCustomParameters'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'properties.uiDefinitionUri', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[WorkspaceProviderAuthorization]'},
        'created_by': {'key': 'properties.createdBy', 'type': 'CreatedBy'},
        'updated_by': {'key': 'properties.updatedBy', 'type': 'CreatedBy'},
        'created_date_time': {'key': 'properties.createdDateTime', 'type': 'iso-8601'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
        'workspace_url': {'key': 'properties.workspaceUrl', 'type': 'str'},
        'storage_account_identity': {'key': 'properties.storageAccountIdentity', 'type': 'ManagedIdentityConfiguration'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.managed_resource_group_id = kwargs.get('managed_resource_group_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.provisioning_state = None
        self.ui_definition_uri = kwargs.get('ui_definition_uri', None)
        self.authorizations = kwargs.get('authorizations', None)
        self.created_by = kwargs.get('created_by', None)
        self.updated_by = kwargs.get('updated_by', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.workspace_id = None
        self.workspace_url = None
        self.storage_account_identity = kwargs.get('storage_account_identity', None)
        self.sku = kwargs.get('sku', None)


class WorkspaceCustomBooleanParameter(Model):
    """The value which should be used for this field.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: bool
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceCustomBooleanParameter, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)


class WorkspaceCustomObjectParameter(Model):
    """The value which should be used for this field.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: object
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceCustomObjectParameter, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)


class WorkspaceCustomParameters(Model):
    """Custom Parameters used for Cluster Creation.

    :param custom_virtual_network_id: The ID of a Virtual Network where this
     Databricks Cluster should be created
    :type custom_virtual_network_id:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_public_subnet_name: The name of a Public Subnet within the
     Virtual Network
    :type custom_public_subnet_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_private_subnet_name: The name of the Private Subnet within
     the Virtual Network
    :type custom_private_subnet_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param enable_no_public_ip: Should the Public IP be Disabled?
    :type enable_no_public_ip:
     ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    :param prepare_encryption: Prepare the workspace for encryption. Enables
     the Managed Identity for managed storage account.
    :type prepare_encryption:
     ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    :param encryption: Contains the encryption details for Customer-Managed
     Key (CMK) enabled workspace.
    :type encryption:
     ~azure.mgmt.databricks.models.WorkspaceEncryptionParameter
    """

    _attribute_map = {
        'custom_virtual_network_id': {'key': 'customVirtualNetworkId', 'type': 'WorkspaceCustomStringParameter'},
        'custom_public_subnet_name': {'key': 'customPublicSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'custom_private_subnet_name': {'key': 'customPrivateSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'enable_no_public_ip': {'key': 'enableNoPublicIp', 'type': 'WorkspaceCustomBooleanParameter'},
        'prepare_encryption': {'key': 'prepareEncryption', 'type': 'WorkspaceCustomBooleanParameter'},
        'encryption': {'key': 'encryption', 'type': 'WorkspaceEncryptionParameter'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceCustomParameters, self).__init__(**kwargs)
        self.custom_virtual_network_id = kwargs.get('custom_virtual_network_id', None)
        self.custom_public_subnet_name = kwargs.get('custom_public_subnet_name', None)
        self.custom_private_subnet_name = kwargs.get('custom_private_subnet_name', None)
        self.enable_no_public_ip = kwargs.get('enable_no_public_ip', None)
        self.prepare_encryption = kwargs.get('prepare_encryption', None)
        self.encryption = kwargs.get('encryption', None)


class WorkspaceCustomStringParameter(Model):
    """The Value.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceCustomStringParameter, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)


class WorkspaceEncryptionParameter(Model):
    """The object that contains details of encryption used on the workspace.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: The value which should be used for this field.
    :type value: ~azure.mgmt.databricks.models.Encryption
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'Encryption'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceEncryptionParameter, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)


class WorkspaceProviderAuthorization(Model):
    """The workspace provider authorization.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. The provider's principal identifier. This
     is the identity that the provider will use to call ARM to manage the
     workspace resources.
    :type principal_id: str
    :param role_definition_id: Required. The provider's role definition
     identifier. This role will define all the permissions that the provider
     must have on the workspace's container resource group. This role
     definition cannot have permission to delete the resource group.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceProviderAuthorization, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)


class WorkspaceUpdate(Model):
    """An update to a workspace.

    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceUpdate, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
