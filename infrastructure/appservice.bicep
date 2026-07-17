param location string
param environment string
param keyVaultUri string
param storageAccountName string


resource plan 'Microsoft.Web/serverfarms@2023-12-01' = {

  name: 'azmcp-plan-${environment}'
  location: location
  sku: {

    name: 'B1'
    tier: 'Basic'

  }
  kind: 'linux'
  properties: {

    reserved: true

  }

}


resource documentApp 'Microsoft.Web/sites@2023-12-01' = {

  name: 'azmcp-document-${environment}-${uniqueString(resourceGroup().id)}'
  location: location
  identity: {

    type: 'SystemAssigned'

  }
  properties: {

    serverFarmId: plan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.12'
      appCommandLine: 'python -m document_server.app'
      appSettings: [
        {
          name: 'SCM_DO_BUILD_DURING_DEPLOYMENT'
          value: 'true'
        }
        {
          name: 'AZURE_STORAGE_ACCOUNT_URL'
          value: 'https://${storageAccountName}.blob.${az.environment().suffixes.storage}/'
        }
        {
          name: 'AZURE_STORAGE_CONTAINER_NAME'
          value: 'documents'
        }
      ]
    }

  }

}


resource employeeApp 'Microsoft.Web/sites@2023-12-01' = {

  name: 'azmcp-employee-${environment}-${uniqueString(resourceGroup().id)}'


  location: location


  identity: {

    type: 'SystemAssigned'

  }


  properties: {

    serverFarmId: plan.id


    siteConfig: {

      linuxFxVersion: 'PYTHON|3.12'


      appCommandLine: 'python -m employee_server.app'


      appSettings: [

        {
          name: 'SCM_DO_BUILD_DURING_DEPLOYMENT'
          value: 'true'
        }

        {
          name: 'DATABASE_URL'

          value: '@Microsoft.KeyVault(SecretUri=${keyVaultUri}secrets/database-url/)'
        }

      ]

    }

  }

}


output documentPrincipalId string = documentApp.identity.principalId

output employeePrincipalId string = employeeApp.identity.principalId

output documentAppName string = documentApp.name

output employeeAppName string = employeeApp.name
