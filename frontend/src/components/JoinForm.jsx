import { useState } from 'react';

function JoinForm({ onJoin }) {

    const [name,setName] = useState('');
    const [room, setRoom] = useState('');

    const handleSubmit = (event) =>{
        event.preventDefault();
        if(room && name){
            onJoin(name,room)
        }
    }

    return (
    <div className="bg-slate-800 p-8 rounded-3xl shadow-2xl w-full max-w-md border border-amber-100">
      <h2 className="text-2xl font-bold mb-6 text-center text-white">Join Meeting</h2>
      
      
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        
        {/* Name Input */}
        <div>
          <label className="block text-sm font-medium text-slate-400 mb-1">Display Name</label>
          <input
            type="text"
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g. John Doe"
            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
          />
        </div>

        {/* Room Code Input */}
        <div>
          <label className="block text-sm font-medium text-slate-400 mb-1">Room Code</label>
          <input
            type="text"
            required
            value={room}
            onChange={(e) => setRoom(e.target.value)}
            placeholder="e.g. ABC-123"
            className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
          />
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="mt-4 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-4 rounded-xl transition-colors shadow-lg shadow-indigo-600/30"
        >
          Join Room
        </button>
      </form>
    </div>
  );

}

export default JoinForm;