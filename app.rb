require 'sinatra'
require 'httparty'
require 'json'
require 'pycall'
generate = PyCall.import_module("generate_poems")

get '/' do
  @available_poets = Dir.children("#{File.dirname(__FILE__)}/input").map { |file| file.split('.')[0] }
  erb :index
end

post '/generate_poem' do
  generate = PyCall.import_module("generate_poems")
  puts params['poet']
  puts params['rhyme']
  content_type :json
  {poem: generate.generate_poem_single_rhyme(params['poet'], params['rhyme'], iterations: 3000, use_tqdm: false)}.to_json
end
