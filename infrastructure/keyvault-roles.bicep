param keyVaultName string
param principalId string


resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' existing = {

  name: keyVaultName

}


resource secretsReaderRole 'Microsoft.Authorization/roleDefinitions@2022-04-01' existing = {

  scope: subscription()
  name: '4633458b-17de-408a-b874-0445c86b69e6'

}


resource assignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {

  name: guid(
    keyVault.id,
    principalId,
    'keyvault-reader'
  )
  scope: keyVault
  properties: {

    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      secretsReaderRole.name
    )
    principalId: principalId
    principalType: 'ServicePrincipal'

  }

}
