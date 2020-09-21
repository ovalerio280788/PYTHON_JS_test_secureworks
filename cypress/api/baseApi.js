export class BaseAPI {
    auth = null;

    /**
     * Constructor of the class, that will create a new authentication object based on the username and password
     * @param username The username of the application
     * @param password The password of the application
     */
    constructor(username, password) {
        this.auth = {
            'user': username,
            'pass': password
        }
    }
}