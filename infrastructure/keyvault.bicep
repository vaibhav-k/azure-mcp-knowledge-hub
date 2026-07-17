param location string


resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {

  name: 'azmcpkv${uniqueString(resourceGroup().id)}'
  location: location
  properties: {

    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    sku: {

      family: 'A'
      name: 'standard'

    }

  }

}


output keyVaultName string = keyVault.name

output keyVaultUri string = keyVault.properties.vaultUri
