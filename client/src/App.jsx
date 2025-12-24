import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'))
  const [isLoginMode, setIsLoginMode] = useState(true)
  const [tasks, setTasks] = useState([]) // State untuk menyimpan daftar tugas
  
  // Data Form Login/Register
  const [formData, setFormData] = useState({ username: '', email: '', password: '' })
  
  // Data Form Tambah Tugas
  const [newTask, setNewTask] = useState({ title: '', description: '' })
  
  const [message, setMessage] = useState('')

  // === EFEK SAMPING: Fetch Tugas saat Token ada ===
  useEffect(() => {
    if (token) {
      fetchTasks()
    }
  }, [token])

  // Fungsi Mengambil Daftar Tugas dari Backend
  const fetchTasks = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/me/tasks', {
        headers: { Authorization: `Bearer ${token}` } // Kirim token sebagai kunci
      })
      setTasks(response.data)
    } catch (error) {
      console.error("Gagal ambil data:", error)
    }
  }

  // Fungsi Tambah Tugas Baru
  const handleAddTask = async (e) => {
    e.preventDefault()
    try {
      await axios.post('http://127.0.0.1:8000/me/tasks', newTask, {
        headers: { Authorization: `Bearer ${token}` }
      })
      setNewTask({ title: '', description: '' }) // Reset form
      fetchTasks() // Refresh daftar tugas
    } catch (error) {
      alert("Gagal menambah tugas")
    }
  }

  // --- LOGIKA FORM USER ---
  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value })
  
  const handleLogin = async (e) => {
    e.preventDefault()
    const params = new URLSearchParams()
    params.append('username', formData.username)
    params.append('password', formData.password)
    try {
      const res = await axios.post('http://127.0.0.1:8000/token', params)
      localStorage.setItem('token', res.data.access_token)
      setToken(res.data.access_token)
    } catch (err) { setMessage("Username/Password Salah!") }
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    try {
      await axios.post('http://127.0.0.1:8000/users/', formData)
      setMessage("Akun dibuat! Silakan Login.")
      setIsLoginMode(true)
    } catch (err) { setMessage("Gagal Daftar (Email mungkin kembar)") }
  }

  const handleLogout = () => {
    localStorage.removeItem('token')
    setToken(null)
    setTasks([])
  }

  // === TAMPILAN DASHBOARD UTAMA ===
  if (token) {
    return (
      <div className="min-h-screen bg-gray-100 p-8">
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <div className="flex justify-between items-center bg-white p-6 rounded-lg shadow mb-6">
            <h1 className="text-2xl font-bold text-blue-600">Task Manager Dashboard</h1>
            <button onClick={handleLogout} className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded">
              Logout
            </button>
          </div>

          {/* Grid Layout: Kiri (Form), Kanan (List) */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            {/* Kolom 1: Form Tambah Tugas */}
            <div className="bg-white p-6 rounded-lg shadow h-fit">
              <h2 className="text-xl font-semibold mb-4">Tambah Tugas</h2>
              <form onSubmit={handleAddTask} className="space-y-4">
                <input 
                  type="text" placeholder="Judul Tugas..." required
                  className="w-full border p-2 rounded"
                  value={newTask.title}
                  onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                />
                <textarea 
                  placeholder="Deskripsi (Opsional)" 
                  className="w-full border p-2 rounded h-24"
                  value={newTask.description}
                  onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                ></textarea>
                <button type="submit" className="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600">
                  + Simpan Tugas
                </button>
              </form>
            </div>

            {/* Kolom 2: Daftar Tugas */}
            <div className="md:col-span-2 space-y-4">
              <h2 className="text-xl font-semibold mb-2">Daftar Tugas Saya ({tasks.length})</h2>
              
              {tasks.length === 0 && (
                <p className="text-gray-500 italic">Belum ada tugas. Yuk buat satu!</p>
              )}

              {tasks.map((task) => (
                <div key={task.id} className="bg-white p-4 rounded-lg shadow border-l-4 border-blue-500 flex justify-between items-start">
                  <div>
                    <h3 className="font-bold text-lg">{task.title}</h3>
                    <p className="text-gray-600">{task.description}</p>
                    <span className="text-xs bg-gray-200 px-2 py-1 rounded mt-2 inline-block">
                      Status: {task.status}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    )
  }

  // === TAMPILAN LOGIN / REGISTER (Sama seperti sebelumnya) ===
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="p-8 bg-white rounded-lg shadow-md w-96">
        <div className="flex justify-between mb-6">
          <button onClick={() => setIsLoginMode(true)} className={`text-lg font-bold ${isLoginMode ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-400'}`}>Masuk</button>
          <button onClick={() => setIsLoginMode(false)} className={`text-lg font-bold ${!isLoginMode ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-400'}`}>Daftar</button>
        </div>
        <form onSubmit={isLoginMode ? handleLogin : handleRegister} className="space-y-4">
          <input type="text" name="username" placeholder="Username" onChange={handleChange} className="w-full border p-2 rounded" required />
          {!isLoginMode && <input type="email" name="email" placeholder="Email" onChange={handleChange} className="w-full border p-2 rounded" required />}
          <input type="password" name="password" placeholder="Password" onChange={handleChange} className="w-full border p-2 rounded" required />
          <button className="w-full bg-blue-600 text-white py-2 rounded">{isLoginMode ? 'Masuk' : 'Daftar'}</button>
        </form>
        {message && <p className="mt-4 text-center text-sm text-red-500">{message}</p>}
      </div>
    </div>
  )
}

export default App