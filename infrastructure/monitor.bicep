param location string

param environment string


resource insights 'Microsoft.Insights/components@2020-02-02' = {

  name: 'azmcp-insights-${environment}-${uniqueString(resourceGroup().id)}'


  location: location


  kind: 'web'


  properties: {

    Application_Type: 'web'

  }

}
