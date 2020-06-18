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


class VSOnlineDelegateAccessTokenRequestBody(Model):
    """Object that includes a VS Online Plans delegate access token request
    parameters.

    All required parameters must be populated in order to send to Azure.

    :param scope: Required. The requested scopes for the VS Online Plan access
     token.
    :type scope: str
    :param expiration: The requested expiration UNIX timestamp (seconds since
     epoch) for the VS Online Plan access token.
    :type expiration: int
    :param identity: Required. The identity of the user of the VS Online Plan
     access token.
    :type identity: ~microsoft.vsonline.models.VSOnlineDelegateIdentity
    :param environment_ids: A subset of environments within the VS Online Plan
     which the returned token will grant access to.  If not provided the token
     will be applicable for all environments.
    :type environment_ids: list[str]
    """

    _validation = {
        'scope': {'required': True},
        'identity': {'required': True},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'expiration': {'key': 'expiration', 'type': 'int'},
        'identity': {'key': 'identity', 'type': 'VSOnlineDelegateIdentity'},
        'environment_ids': {'key': 'environmentIds', 'type': '[str]'},
    }

    def __init__(self, *, scope: str, identity, expiration: int=None, environment_ids=None, **kwargs) -> None:
        super(VSOnlineDelegateAccessTokenRequestBody, self).__init__(**kwargs)
        self.scope = scope
        self.expiration = expiration
        self.identity = identity
        self.environment_ids = environment_ids
