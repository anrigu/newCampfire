import a from 'axios';

export default a.create({
    baseURL: 'http://localhost:8000/', //`${process.env.REACT_APP_REST_API_URL}`,
    withCredentials: true,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'x-csrftoken',
    validateStatus: () => true
});