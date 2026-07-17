param storageAccountName string

param documentAppPrincipalId string


resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {

  name: storageAccountName

}


resource blobReaderRoleDefinition 'Microsoft.Authorization/roleDefinitions@2022-04-01' existing = {

  scope: subscription()

  name: '2a2b9908-6ea1-4ae2-8e65-a410df84e7d1'

}


resource blobReaderAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {

  name: guid(
    storageAccount.id,
    documentAppPrincipalId,
    'blob-reader'
  )


  scope: storageAccount


  properties: {

    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      blobReaderRoleDefinition.name
    )


    principalId: documentAppPrincipalId


    principalType: 'ServicePrincipal'

  }

}
