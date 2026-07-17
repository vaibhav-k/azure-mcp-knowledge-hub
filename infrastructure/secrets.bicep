param keyVaultName string
param databaseUrl string


resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' existing = {

  name: keyVaultName

}


resource databaseSecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {

  parent: keyVault

  name: 'database-url'

  properties: {

    value: databaseUrl

  }

}
