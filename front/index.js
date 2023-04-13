const DOMAIN = 'http://localhost:';
const PORT = 5001;
// Resources
const RESOURCE = 'names';
const POST_ROUTE = 'post_endpoint';
// Elements
const listContainer = document.querySelector('.names-list');
console.log(listContainer);

const populateNamesList = (namesList) => {
  namesList.forEach(le => {
    //Create the HTML element
    const listItem = document.createElement('li');
    listItem.innerText = le;
    // Add to the container
    listContainer.appendChild(listItem);
  });
}

// fetch(`${DOMAIN}${PORT}/${RESOURCE}`)
//   .then(raw => raw.json())
//   .then(response => {
//     //logic
//     populateNamesList(response.names);
//   })
//   .catch(e => console.log(e));

const getMain = async () => {
  try {
    const raw = await fetch(`${DOMAIN}${PORT}/${RESOURCE}`);
    const response = await raw.json();
    populateNamesList(response.names);
  } catch (error) {
    console.log(error);
  }
}

const postEndpoint = async () => {
  try {
    const raw = await fetch(
      `${DOMAIN}${PORT}/${POST_ROUTE}`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'person1': 'Olivia',
          'person2': 'Sophia'
        })
      }
    );
    const response = await raw.json();
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

getMain();
postEndpoint();
