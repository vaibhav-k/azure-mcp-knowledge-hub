param location string

param environment string


resource vault 'Microsoft.KeyVault/vaults@2023-07-01' = {

  name: 'azmcp-kv-${environment}-${uniqueString(resourceGroup().id)}'


  location: location


  properties: {

    tenantId: subscription().tenantId


    sku: {

      family: 'A'

      name: 'standard'

    }


    enableRbacAuthorization: true

  }

}
