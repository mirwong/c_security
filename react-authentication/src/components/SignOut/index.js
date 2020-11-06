/* jshint esversion: 6 */

import React from 'react';

import { withFirebase } from '../Firebase';

// signOutBind = () => {
//     firebase.doSignOut().bind(firebase);
// }

const SignOutButton = ({ firebase }) => (
  <button type="button" onClick={() => firebase.doSignOut(firebase)}>
    Sign Out
  </button>
);

export default withFirebase(SignOutButton);
