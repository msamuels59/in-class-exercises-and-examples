import { Route, Routes } from 'react-router-dom'

import AllMeetupsPage from './pages/AllMeetups';
import NewMeetupsPage from './pages/NewMeetups';
import Favorites from './pages/Favorites';
import Layout from './components/layouts/Layout';



function App() {
  return (
      <Layout>
      <Routes>
        <Route path='/' element={<AllMeetupsPage />} />
        <Route path='/new-meetup' element={<NewMeetupsPage />} />
        <Route path='/favorites' element={<Favorites />} />
      </Routes>
      </Layout>
  );
}

export default App;
