export const apiKey = () => (process.env.NODE_ENV === 'development'
    ? '83ee45ca-7023-4dc5-8670-e2fdbb48b405'
    : '34df2962-0a87-486a-8e21-cb734ca49405');

// environment url with cors proxy
export const envUrl = () => (process.env.NODE_ENV === 'development'
    ? 'https://cors-anywhere.herokuapp.com/https://sandbox-api.coinmarketcap.com/'
    : 'https://cors-anywhere.herokuapp.com/https://pro-api.coinmarketcap.com/');
