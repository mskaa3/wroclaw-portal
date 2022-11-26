import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../../css/Currency.css';

const CurrencyTable = () => {
  const [tablearray, setTableArray] = useState();
  console.log(tablearray);

  useEffect(() => {
    const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';
    axios.get(`${API_URL}/currency`).then((resp) => {
      setTableArray(resp.data);
    });
    /*const asyncTry = async () => {
      
      try {
        const res = await axios.get(`${API_URL}/currency`);
        console.log(res.data);
        setTableArray(res.data);
      } catch (e) {
        console.log(e);
      }
    //};
    asyncTry();*/
  }, []);
  console.log(tablearray);
  console.log(tablearray?.centkantor);
  return (
    <div>
      <center>
        <table className="tableA">
          <thead>
            <tr>
              <th>Currency</th>
              <th>Buy Rate</th>
              <th>Sell Rate</th>
              <th>Currency</th>
              <th>Buy Rate</th>
              <th>Sell Rate</th>
              <th>Exchange Web-Page</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{tablearray?.centkantor[0]}</td>
              <td>{tablearray?.centkantor[1]}</td>
              <td>{tablearray?.centkantor[2]}</td>
              <td>{tablearray?.centkantor[3]}</td>
              <td>{tablearray?.centkantor[4]}</td>
              <td>{tablearray?.centkantor[5]}</td>
              <td>
                <a
                  href="https://www.centkantor.pl/"
                  target="_blank"
                  rel="noreferrer"
                >
                  centkantor
                </a>
              </td>
            </tr>
            <tr>
              <td>{tablearray?.kantorplex[0]}</td>
              <td>{tablearray?.kantorplex[1]}</td>
              <td>{tablearray?.kantorplex[2]}</td>
              <td>{tablearray?.kantorplex[3]}</td>
              <td>{tablearray?.kantorplex[4]}</td>
              <td>{tablearray?.kantorplex[5]}</td>
              <td>
                <a
                  href="https://kantorplex.pl/"
                  target="_blank"
                  rel="noreferrer"
                >
                  kantorplex
                </a>
              </td>
            </tr>
            <tr>
              <td>{tablearray?.kantorpolonez[0]}</td>
              <td>{tablearray?.kantorpolonez[1]}</td>
              <td>{tablearray?.kantorpolonez[2]}</td>
              <td>{tablearray?.kantorpolonez[3]}</td>
              <td>{tablearray?.kantorpolonez[4]}</td>
              <td>{tablearray?.kantorpolonez[5]}</td>
              <td>
                <a
                  href="http://www.kantorpolonez.pl/"
                  target="_blank"
                  rel="noreferrer"
                >
                  kantorpolonez
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </center>
    </div>
  );
};

export default CurrencyTable;
